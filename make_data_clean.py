"""Build Data_clean/ from the raw Data/ folder (the fixes are listed in data_fixes.md).
Run once before run_all.py:   python3 make_data_clean.py
"""
import os, shutil, re

SRC, DST = "Data", "Data_clean"
RENAME_MODEL = {"GitHub-Copilot": "Copilot"}
RENAME_VARIANT = {"orginal": "original"}

if os.path.exists(DST):
    shutil.rmtree(DST)
n = 0
for model in sorted(os.listdir(SRC)):
    mp = os.path.join(SRC, model)
    if not os.path.isdir(mp):
        continue
    for variant in sorted(os.listdir(mp)):
        vp = os.path.join(mp, variant)
        if not os.path.isdir(vp) or variant == "__pycache__":
            continue
        out = os.path.join(DST, RENAME_MODEL.get(model, model), RENAME_VARIANT.get(variant, variant))
        os.makedirs(out)
        for f in sorted(os.listdir(vp)):
            if re.fullmatch(r"task\d+\.py", f):          # drops __pycache__ and stray requirements.txt
                shutil.copy(os.path.join(vp, f), os.path.join(out, f))
                n += 1

# fix: Gemini/typo/task18.py had real newline characters inside "\n" and "\r" string literals (copy artifact)
p = os.path.join(DST, "Gemini", "typo", "task18.py")
s = open(p, encoding="utf-8", newline="").read()
s = s.replace('"\n"', '"\\n"').replace('"\r"', '"\\r"')
open(p, "w", encoding="utf-8", newline="").write(s)

print(f"Data_clean created with {n} task files (expected 400).")
