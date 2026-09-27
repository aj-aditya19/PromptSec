"""Detailed per-file security screening with optional Bandit integration."""
import ast
import json
import re
import shutil
import subprocess
from pathlib import Path

SECRET_RE = re.compile(r"(?i)(password|passwd|api[_-]?key|secret|token)\\s*[:=]\\s*['\"][^'\"]{6,}['\"]")


def inspect(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    result = {"file": str(path), "bare_except": bool(re.search(r"(?m)^\\s*except\\s*:\\s*$", text)), "hardcoded_secret": bool(SECRET_RE.search(text)), "syntax_error": None, "try_blocks": 0}
    try:
        tree = ast.parse(text)
        result["try_blocks"] = sum(isinstance(node, ast.Try) for node in ast.walk(tree))
    except SyntaxError as error:
        result["syntax_error"] = str(error)
    return result


def main() -> None:
    root = Path(__file__).resolve().parent
    files = sorted(root.glob("**/rep_*.py"))
    findings = [inspect(path) for path in files]
    output = root / "analysis_output"
    output.mkdir(exist_ok=True)
    (output / "detailed_security_findings.json").write_text(json.dumps(findings, indent=2), encoding="utf-8")
    bandit = shutil.which("bandit")
    if bandit and files:
        report = output / "bandit_report.json"
        subprocess.run([bandit, "-r", *[str(path) for path in files], "-f", "json", "-o", str(report)], check=False)
        print(f"Bandit report: {report}")
    else:
        print("Bandit not installed or no samples found; built-in scan completed.")
    print(f"Detailed findings: {output / 'detailed_security_findings.json'}")


if __name__ == "__main__":
    main()
