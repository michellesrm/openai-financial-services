from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
for p in [root/'plugin.json', root/'.codex-plugin'/'plugin.json']:
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f"{p}: invalid JSON: {e}")
skills=list((root/'skills').glob('*/SKILL.md'))
if not skills: errors.append('No skills found')
for p in skills:
    s=p.read_text()
    m=re.match(r'^---\n(.*?)\n---\n',s,re.S)
    if not m: errors.append(f'{p}: missing YAML-like frontmatter'); continue
    fm=m.group(1)
    if 'name:' not in fm or 'description:' not in fm: errors.append(f'{p}: missing name/description')
    name=re.search(r'^name:\s*(.+)$',fm,re.M)
    if name and name.group(1).strip()!=p.parent.name: errors.append(f'{p}: name does not match folder')
print(f'Validated {len(skills)} skills')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK')
