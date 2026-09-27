#!/usr/bin/env python3
"""Create the PromptSec Phase 2 directory template."""

from pathlib import Path
import argparse

TASKS = [
    "Reverse Linked List",
    "Two Sum",
    "Valid Parentheses",
    "Binary Search",
    "Merge Intervals",
    "Longest Substring Without Repeating Characters",
    "Detect Cycle in Linked List",
    "Top K Frequent Elements",
    "Number of Islands",
    "Dijkstra's Shortest Path",
    "JWT Authentication",
    "BFS Graph Traversal",
]
VARIANTS = ["original", "typo", "synonym", "paraphrase"]

def create_template(root: Path) -> int:
    count = 0
    for task in TASKS:
        for variant in VARIANTS:
            for rep in range(1, 5):
                path = root / task / variant / f"rep_{rep}.py"
                path.parent.mkdir(parents=True, exist_ok=True)
                if not path.exists():
                    path.write_text(
                        f"# PromptSec placeholder\n"
                        f"# Replace this file with the model-generated Python code.\n"
                        f"# Task: {task}\n"
                        f"# Variant: {variant}\n"
                        f"# Repetition: {rep}\n",
                        encoding="utf-8",
                    )
                    count += 1
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="ChatGPT")
    parser.add_argument("--root", default=None)
    args = parser.parse_args()

    root = Path(args.root) if args.root else Path(f"generated_code_{args.model}")
    created = create_template(root)
    print(f"Created/verified template: {root}")
    print(f"New placeholder files created: {created}")
    print("Expected dataset size: 192 Python files.")

if __name__ == "__main__":
    main()
