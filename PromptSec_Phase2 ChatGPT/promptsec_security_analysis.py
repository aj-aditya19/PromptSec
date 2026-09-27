#!/usr/bin/env python3
"""Optional Bandit-based deep security scan for PromptSec samples."""

from pathlib import Path
import argparse
import json
import subprocess
import sys

def scan_file(path: Path):
    cmd = [
        sys.executable, "-m", "bandit",
        "-q", "-f", "json", str(path)
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:
        return {"path": str(path), "bandit_available": False, "error": str(exc)}

    if proc.returncode not in (0, 1):
        return {
            "path": str(path), "bandit_available": True,
            "error": proc.stderr.strip() or f"Bandit exit code {proc.returncode}"
        }

    try:
        data = json.loads(proc.stdout or "{}")
    except json.JSONDecodeError:
        return {
            "path": str(path), "bandit_available": True,
            "error": "Bandit returned non-JSON output.",
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }

    return {
        "path": str(path),
        "bandit_available": True,
        "metrics": data.get("metrics", {}),
        "results": data.get("results", []),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="generated_code_ChatGPT")
    parser.add_argument("--output", default="bandit_results")
    args = parser.parse_args()

    root, out = Path(args.root), Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    files = sorted(root.glob("*/*/rep_*.py"))
    report = [scan_file(path) for path in files]

    output = out / "bandit_results.json"
    output.write_text(json.dumps({
        "root": str(root),
        "files_scanned": len(files),
        "results": report,
        "note": "Bandit findings require manual interpretation; absence of findings does not prove security."
    }, indent=2), encoding="utf-8")

    unavailable = sum(not x.get("bandit_available", False) for x in report)
    print(f"Scanned {len(files)} files.")
    print(f"Bandit unavailable/errors for {unavailable} files.")
    print(f"Wrote: {output}")

if __name__ == "__main__":
    main()
