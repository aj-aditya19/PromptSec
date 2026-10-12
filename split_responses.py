"""Split saved model answers into task files.

Input : responses/<model>/<variant>.txt   (whole answer pasted from the chat)
Output: ai_code/<model>/<variant>/task1.py ... task20.py
Run   : python split_responses.py
"""
import re, sys
from pathlib import Path

MODELS = ["claude", "chatgpt", "gemini", "copilot", "perplexity"]
VARIANTS = ["original", "typo", "synonym", "paraphrase"]
FENCE = re.compile(r"```[a-zA-Z0-9]*[ \t]*\r?\n(.*?)\r?\n```", re.S)
MARK = re.compile(r"FILE:\s*task\s*0*(\d+)(?:\.py)?", re.I)

def split(text):
    text = text.replace("\r\n", "\n")
    blocks = [(m.start(), m.group(1)) for m in FENCE.finditer(text)]
    marks = [(m.start(), int(m.group(1))) for m in MARK.finditer(text)]
    found = {}
    for pos, n in marks:
        nxt = next((b for b in blocks if b[0] > pos), None)
        if nxt and n not in found:
            found[n] = nxt[1]
    warn = ""
    if len(found) < 20 and len(blocks) == 20:
        found = {i + 1: b[1] for i, b in enumerate(blocks)}
        warn = " (markers missing, used block order)"
    return found, warn

def main():
    root = Path(".")
    total_missing = 0
    for m in MODELS:
        for v in VARIANTS:
            f = root / "responses" / m / f"{v}.txt"
            if not f.exists():
                print(f"[skip]    {m}/{v}: no file")
                continue
            found, warn = split(f.read_text(encoding="utf-8", errors="ignore"))
            out = root / "ai_code" / m / v
            out.mkdir(parents=True, exist_ok=True)
            for n, code in found.items():
                (out / f"task{n}.py").write_text(code.strip() + "\n", encoding="utf-8")
            missing = [n for n in range(1, 21) if n not in found]
            total_missing += len(missing)
            status = "OK" if not missing else f"MISSING tasks {missing}"
            print(f"[{status}] {m}/{v}: {len(found)}/20 files{warn}")
    print("\nDone. Missing total:", total_missing)

if __name__ == "__main__":
    main()
