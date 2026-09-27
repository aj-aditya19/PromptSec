"""Create or verify the PromptSec Phase 2 sample directory template."""
from pathlib import Path

TASKS = [
    "Reverse Linked List", "Two Sum", "Valid Parentheses", "Binary Search",
    "Merge Intervals", "Longest Substring Without Repeating Characters",
    "Detect Cycle in Linked List", "Top K Frequent Elements", "Number of Islands",
    "Dijkstra's Shortest Path", "JWT Authentication", "BFS Graph Traversal",
]
VARIANTS = ["original", "typo", "synonym", "paraphrase"]


def main() -> None:
    root = Path(__file__).resolve().parent
    created = 0
    for task in TASKS:
        for variant in VARIANTS:
            directory = root / task / variant
            if not directory.exists():
                directory.mkdir(parents=True)
                created += 1
    print(f"Template ready: {root}")
    print(f"Tasks: {len(TASKS)}, variants: {len(VARIANTS)}, expected samples: {len(TASKS) * len(VARIANTS) * 4}")
    print(f"Directories created during this run: {created}")


if __name__ == "__main__":
    main()
