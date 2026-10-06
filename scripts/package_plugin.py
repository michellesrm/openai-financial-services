from pathlib import Path
import shutil, zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"dist"
STAGE=OUT/"financial-services-workflows"
if OUT.exists(): shutil.rmtree(OUT)
STAGE.mkdir(parents=True)

include=["plugin.json",".codex-plugin","skills","assets","LICENSE","NOTICE.md","README.md","INSTALL.md"]
for rel in include:
    src=ROOT/rel
    dst=STAGE/rel
    if src.is_dir(): shutil.copytree(src,dst)
    elif src.exists():
        dst.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(src,dst)

zip_path=OUT/"financial-services-workflows.zip"
with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    for p in STAGE.rglob("*"):
        if p.is_file():
            z.write(p,p.relative_to(OUT))
print(zip_path)
