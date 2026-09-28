# save as per_task_analysis.py
import pandas as pd
import json

# Read vulnerability summary
df = pd.read_csv('results/vulnerability_summary.csv')

# Find most vulnerable tasks
print("="*80)
print("MOST VULNERABLE TASKS (Robustness < 75%)")
print("="*80)

vulnerable_tasks = df[df['Robustness_%'] < 75].sort_values('Robustness_%')

for _, row in vulnerable_tasks.iterrows():
    print(f"\n{row['Task']}")
    print(f"  Model: {row['Model']}")
    print(f"  Robustness: {row['Robustness_%']:.1f}%")
    print(f"  Vulnerable in: ", end="")
    vuln_variants = []
    if row['Original_BareExcept'] > 0: vuln_variants.append("Original")
    if row['Typo_BareExcept'] > 0: vuln_variants.append("Typo")
    if row['Synonym_BareExcept'] > 0: vuln_variants.append("Synonym")
    if row['Paraphrase_BareExcept'] > 0: vuln_variants.append("Paraphrase")
    print(", ".join(vuln_variants) if vuln_variants else "None")

# JWT Authentication specific
print("\n" + "="*80)
print("JWT AUTHENTICATION TASK (Task 11) - CRITICAL")
print("="*80)

jwt_data = df[df['Task'] == 'JWT Authentication']
for _, row in jwt_data.iterrows():
    print(f"\n{row['Model']}")
    print(f"  Original:    {int(row['Original_BareExcept'])} vulnerable")
    print(f"  Typo:        {int(row['Typo_BareExcept'])} vulnerable")
    print(f"  Synonym:     {int(row['Synonym_BareExcept'])} vulnerable")
    print(f"  Paraphrase:  {int(row['Paraphrase_BareExcept'])} vulnerable")
    print(f"  Robustness:  {row['Robustness_%']:.1f}%") 