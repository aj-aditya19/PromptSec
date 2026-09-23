import json, os

def parse_bandit(filepath):
    with open(filepath) as f:
        data = json.load(f)
    file_results = {}
    for result in data.get("results", []):
        fname = os.path.basename(result["filename"])
        if fname not in file_results:
            file_results[fname] = {"count": 0, "high": 0, "medium": 0, "low": 0, "types": []}
        file_results[fname]["count"] += 1
        sev = result["issue_severity"].lower()
        file_results[fname][sev] = file_results[fname].get(sev, 0) + 1
        file_results[fname]["types"].append(result["test_name"])
    return file_results

models = ["claude_code", "chatgpt_code", "gemini", "github_copilot", "perplexity"]
variants = ["original", "typo", "synonym", "paraphrase"]

all_data = {}
all_data["Human"] = parse_bandit("results/bandit_human.json")
for model in models:
    for variant in variants:
        key = f"{model}__{variant}"
        all_data[key] = parse_bandit(f"results/bandit_{model}_{variant}.json")

# Summary table: total issues per model per variant
print(f"{'Model':<18} {'Original':<10} {'Typo':<10} {'Synonym':<10} {'Paraphrase':<12}")
print("-" * 65)
for model in models:
    row = [model]
    for variant in variants:
        key = f"{model}__{variant}"
        total = sum(f["count"] for f in all_data[key].values())
        row.append(str(total))
    print(f"{row[0]:<18} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<12}")

human_total = sum(f["count"] for f in all_data["Human"].values())
print(f"\nHuman baseline total issues: {human_total}")

with open("results/all_parsed.json", "w") as f:
    json.dump(all_data, f, indent=2)

print("\n=== Detailed issue types found (non-human) ===")
seen_types = set()
for key, files in all_data.items():
    for fname, info in files.items():
        for t in info["types"]:
            seen_types.add(t)
print(seen_types)
