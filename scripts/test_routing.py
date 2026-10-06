from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
skills = {}
for p in (ROOT / "skills").glob("*/SKILL.md"):
    text = p.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        continue
    name = re.search(r"^name:\s*(.+)$", fm.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", fm.group(1), re.M)
    if name:
        skills[name.group(1).strip()] = (desc.group(1).strip() if desc else "")

rules = json.loads((ROOT/"skills/finance-router/references/routing-rules.json").read_text())
evals = json.loads((ROOT/"tests/routing_evals.json").read_text())
errors=[]

for route in rules["routes"]:
    for key in [route["primary"], *route.get("support",[])]:
        if key not in skills:
            errors.append(f"routing rule {route['id']} references missing skill {key}")

for case in evals["cases"]:
    primary=case.get("expected_primary")
    if primary is not None and primary not in skills:
        errors.append(f"eval references missing primary skill {primary}")
    for key in case.get("expected_support",[]):
        if key not in skills:
            errors.append(f"eval references missing support skill {key}")

# Descriptions are the native discovery surface; require useful length and explicit when-to-use language.
for name, desc in skills.items():
    if len(desc) < 35:
        errors.append(f"{name}: description too short for reliable discovery")
    if name == "finance-router" and not any(x in desc.lower() for x in ["broad","multi-step","ambiguous"]):
        errors.append("finance-router: description must constrain router activation")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(skills)} skills, {len(rules['routes'])} routing rules, {len(evals['cases'])} routing eval cases")
