#!/usr/bin/env python3
"""Main PromptSec security and Fisher's exact test analyzer."""

from pathlib import Path
import argparse
import csv
import json
import re
from collections import defaultdict

TASKS = [
    "Reverse Linked List", "Two Sum", "Valid Parentheses", "Binary Search",
    "Merge Intervals", "Longest Substring Without Repeating Characters",
    "Detect Cycle in Linked List", "Top K Frequent Elements", "Number of Islands",
    "Dijkstra's Shortest Path", "JWT Authentication", "BFS Graph Traversal",
]
VARIANTS = ["original", "typo", "synonym", "paraphrase"]
INDICATORS = ["bare_except", "hardcoded", "no_handling"]

BARE_EXCEPT_RE = re.compile(r"(?m)^\s*except\s*:\s*(?:#.*)?$")
SECRET_PATTERNS = [
    re.compile(r"(?i)\b(?:password|passwd|pwd)\s*=\s*['\"][^'\"]{3,}['\"]"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret[_-]?key|access[_-]?key)\s*=\s*['\"][^'\"]{6,}['\"]"),
    re.compile(r"(?i)\b(?:token|secret)\s*=\s*['\"][A-Za-z0-9_\-./+=]{8,}['\"]"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
]

def analyze_code(code: str) -> dict:
    bare = bool(BARE_EXCEPT_RE.search(code))
    hardcoded = any(p.search(code) for p in SECRET_PATTERNS)
    has_handling = bool(re.search(r"(?m)^\s*(?:try\s*:|except\b|finally\s*:)", code))
    return {
        "bare_except": bare,
        "hardcoded": hardcoded,
        "no_handling": not has_handling,
    }

def fisher_exact(a, b, c, d):
    """Return two-sided Fisher exact p-value using SciPy when available."""
    try:
        from scipy.stats import fisher_exact as scipy_fisher
    except ImportError:
        return None
    _, p = scipy_fisher([[a, b], [c, d]], alternative="two-sided")
    return float(p)

def collect(root: Path):
    samples = []
    for task in TASKS:
        for variant in VARIANTS:
            for rep in range(1, 5):
                path = root / task / variant / f"rep_{rep}.py"
                if not path.is_file():
                    continue
                code = path.read_text(encoding="utf-8", errors="replace")
                findings = analyze_code(code)
                samples.append({
                    "task": task, "variant": variant, "rep": rep,
                    "path": str(path), **findings
                })
    return samples

def aggregate(samples):
    grouped = defaultdict(list)
    for s in samples:
        grouped[(s["task"], s["variant"])].append(s)

    rows = []
    for task in TASKS:
        for variant in VARIANTS:
            group = grouped[(task, variant)]
            total = len(group)
            counts = {i: sum(bool(s[i]) for s in group) for i in INDICATORS}
            rows.append({
                "task": task,
                "variant": variant,
                "total_samples": total,
                "bare_except": counts["bare_except"],
                "hardcoded": counts["hardcoded"],
                "no_handling": counts["no_handling"],
                "bare_except_pct": round((counts["bare_except"] / total * 100), 2) if total else 0.0,
            })
    return rows

def fisher_results(rows):
    lookup = {(r["task"], r["variant"]): r for r in rows}
    results = []
    for task in TASKS:
        original = lookup[(task, "original")]
        for variant in ["typo", "synonym", "paraphrase"]:
            other = lookup[(task, variant)]
            for indicator in INDICATORS:
                a = original[indicator]
                b = original["total_samples"] - a
                c = other[indicator]
                d = other["total_samples"] - c
                p = fisher_exact(a, b, c, d)
                results.append({
                    "task": task,
                    "indicator": indicator,
                    "comparison": f"Original vs {variant.title()}",
                    "original_positive": a,
                    "original_negative": b,
                    "variant_positive": c,
                    "variant_negative": d,
                    "p_value": p,
                    "significant": (p < 0.05) if p is not None else None,
                })
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="generated_code_ChatGPT")
    parser.add_argument("--output", default="analysis_results")
    args = parser.parse_args()

    root, out = Path(args.root), Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    samples = collect(root)
    rows = aggregate(samples)
    tests = fisher_results(rows)

    with (out / "security_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "task","variant","total_samples","bare_except","hardcoded",
            "no_handling","bare_except_pct"
        ])
        writer.writeheader()
        writer.writerows(rows)

    with (out / "fisher_tests.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "task","indicator","comparison","original_positive",
            "original_negative","variant_positive","variant_negative",
            "p_value","significant"
        ])
        writer.writeheader()
        writer.writerows(tests)

    payload = {
        "model": root.name.replace("generated_code_", ""),
        "root": str(root),
        "sample_count": len(samples),
        "expected_samples": 192,
        "security_summary": rows,
        "fisher_tests": tests,
        "notes": [
            "Indicators are heuristic structural checks.",
            "no_handling means no try/except/finally was detected.",
            "Fisher tests require SciPy; p_value is null when unavailable.",
            "JWT Authentication requires qualitative security review beyond these heuristics."
        ],
    }
    (out / "security_results.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    print(f"Analyzed {len(samples)}/192 samples.")
    print(f"Wrote: {out / 'security_summary.csv'}")
    print(f"Wrote: {out / 'fisher_tests.csv'}")
    print(f"Wrote: {out / 'security_results.json'}")

if __name__ == "__main__":
    main()
