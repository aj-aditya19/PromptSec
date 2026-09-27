"""Validate PromptSec task/variant directories and repetition counts."""
from pathlib import Path

TASKS = [
    "Reverse Linked List", "Two Sum", "Valid Parentheses", "Binary Search",
    "Merge Intervals", "Longest Substring Without Repeating Characters",
    "Detect Cycle in Linked List", "Top K Frequent Elements", "Number of Islands",
    "Dijkstra's Shortest Path", "JWT Authentication", "BFS Graph Traversal",
]
VARIANTS = ["original", "typo", "synonym", "paraphrase"]
EXPECTED = {f"rep_{index}.py" for index in range(1, 5)}


def main() -> int:
    root = Path(__file__).resolve().parent
    total = 0
    incomplete = 0
    for task in TASKS:
        for variant in VARIANTS:
            directory = root / task / variant
            files = {path.name for path in directory.glob("*.py")} if directory.exists() else set()
            missing = sorted(EXPECTED - files)
            extra = sorted(files - EXPECTED)
            total += len(files & EXPECTED)
            if missing or extra:
                incomplete += 1
                print(f"INCOMPLETE | {task} | {variant} | missing={missing} extra={extra}")
            else:
                print(f"OK         | {task} | {variant}")
    print(f"\nExpected: 192 | Found expected files: {total} | Incomplete cells: {incomplete}")
    return 0 if total == 192 and incomplete == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
