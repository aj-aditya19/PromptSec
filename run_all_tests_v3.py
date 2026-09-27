import sys
sys.path.insert(0, '.')
from robust_test_v3 import run_all
import json

models = ["claude_code", "chatgpt_code", "gemini", "github_copilot", "perplexity"]
variants = ["original", "typo", "synonym", "paraphrase"]

human_files = {
    1: "task1_reverse_linkedlist.py", 2: "task2_two_sum.py", 3: "task3_valid_parentheses.py",
    4: "task4_binary_search.py", 5: "task5_merge_intervals.py", 6: "task6_longest_substring.py",
    7: "task7_detect_cycle.py", 8: "task8_top_k_frequent.py", 9: "task9_number_islands.py",
    10: "task10_dijkstra.py", 11: "task11_jwt_auth.py", 12: "task12_bfs.py"
}

jobs = []
# human (skip task 1,7,12 which use different API structure - tested separately before)
for tid in [2,3,4,5,6,8,9,11]:
    jobs.append(("Human", f"human_code/{human_files[tid]}", tid))

for model in models:
    for variant in variants:
        for tid in range(1, 13):
            jobs.append((f"{model}__{variant}", f"{model}/{variant}/task{tid}.py", tid))

results = run_all(jobs)

# Print grouped summary
from collections import defaultdict
summary = defaultdict(lambda: [0, 0])
fails_detail = []
for label, task, res, msg in results:
    if res == "PASS":
        summary[label][0] += 1
    else:
        summary[label][1] += 1
        fails_detail.append((label, task, msg))

print(f"{'Label':<30} {'Pass':<6} {'Fail':<6}")
print("-" * 45)
for label, (p, f) in sorted(summary.items()):
    print(f"{label:<30} {p:<6} {f:<6}")

print("\n=== FAILURES DETAIL ===")
for label, task, msg in fails_detail:
    print(f"{label:<30} {task:<8} {msg}")

with open("results/functional_all.json", "w") as f:
    json.dump(results, f, indent=2)
