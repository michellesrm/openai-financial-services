from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors=[]

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{path}: invalid JSON: {e}")
        return {}

portable=load_json(ROOT/"plugin.json")
codex=load_json(ROOT/".codex-plugin"/"plugin.json")
inventory=load_json(ROOT/"SKILL_INVENTORY.json")
marketplace=load_json(ROOT/".agents"/"plugins"/"marketplace.json")

if portable.get("$schema")!="https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
    errors.append("plugin.json: missing/incorrect Agent Plugins schema")
if portable.get("name")!="financial-services-workflows":
    errors.append("plugin.json: unexpected plugin name")
if portable.get("version")!=codex.get("version") or portable.get("version")!=inventory.get("version"):
    errors.append("version mismatch across plugin.json, Codex manifest, and inventory")
if codex.get("skills")!="./skills/":
    errors.append(".codex-plugin/plugin.json: skills must point to ./skills/")

plugins=marketplace.get("plugins",[])
if len(plugins)!=1:
    errors.append("marketplace must expose exactly one plugin")
else:
    entry=plugins[0]
    if entry.get("name")!="financial-services-workflows":
        errors.append("marketplace plugin name mismatch")
    if entry.get("source",{}).get("source")!="url":
        errors.append("marketplace source should use Git URL for repository-root plugin")
    if not entry.get("source",{}).get("url","").endswith("openai-financial-services.git"):
        errors.append("marketplace Git URL mismatch")

skills={}
for p in sorted((ROOT/"skills").glob("*/SKILL.md")):
    s=p.read_text(encoding="utf-8")
    m=re.match(r"^---\n(.*?)\n---\n",s,re.S)
    if not m:
        errors.append(f"{p}: missing YAML-like frontmatter")
        continue
    fm=m.group(1)
    name=re.search(r"^name:\s*(.+)$",fm,re.M)
    desc=re.search(r"^description:\s*(.+)$",fm,re.M)
    if not name or not desc:
        errors.append(f"{p}: missing name/description")
        continue
    skill_name=name.group(1).strip()
    description=desc.group(1).strip()
    if skill_name!=p.parent.name:
        errors.append(f"{p}: name does not match folder")
    if len(description)<35:
        errors.append(f"{p}: description is too short for reliable discovery")
    skills[skill_name]=description

listed=inventory.get("skills",[])
if inventory.get("skill_count")!=len(skills):
    errors.append(f"inventory count {inventory.get('skill_count')} != discovered skills {len(skills)}")
if sorted(listed)!=sorted(skills):
    errors.append("SKILL_INVENTORY.json does not match discovered skills")
if "finance-router" not in skills:
    errors.append("finance-router skill missing")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: plugin v{portable.get('version')} with {len(skills)} skills")
