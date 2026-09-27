#!/usr/bin/env python3
"""Validate the PromptSec generated-code directory structure."""

from pathlib import Path
import argparse

TASKS = [
    "Reverse Linked List", "Two Sum", "Valid Parentheses", "Binary Search",
    "Merge Intervals", "Longest Substring Without Repeating Characters",
    "Detect Cycle in Linked List", "Top K Frequent Elements", "Number of Islands",
    "Dijkstra's Shortest Path", "JWT Authentication", "BFS Graph Traversal",
]
VARIANTS = ["original", "typo", "synonym", "paraphrase"]

def validate(root: Path) -> bool:
    total = 0
    complete_groups = 0
    incomplete = []

    for task in TASKS:
        for variant in VARIANTS:
            missing = []
            for rep in range(1, 5):
                path = root / task / variant / f"rep_{rep}.py"
                if not path.is_file():
                    missing.append(f"rep_{rep}.py")
                else:
                    total += 1
            if not missing:
                complete_groups += 1
            else:
                incomplete.append((task, variant, missing))

    print(f"Root: {root}")
    print(f"Samples present: {total}/192")
    print(f"Complete task/variant groups: {complete_groups}/48")

    if incomplete:
        print("\nIncomplete groups:")
        for task, variant, missing in incomplete:
            print(f"  {task} / {variant}: missing {', '.join(missing)}")
    else:
        print("\nAll 192 expected sample files are present.")

    return total == 192 and not incomplete

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="generated_code_ChatGPT")
    args = parser.parse_args()
    ok = validate(Path(args.root))
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
