#!/usr/bin/env python3
"""
PromptSec Batch Security & Statistical Analyzer
Model: Gemini
"""

import os
import json
import csv
import sys
from promptsec_security_analysis import analyze_code_file

try:
    from scipy.stats import fisher_exact
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

MODEL_NAME = "Gemini"
BASE_DIR = f"generated_code_{MODEL_NAME}"
VARIANTS = ["original", "typo", "synonym", "paraphrase"]

def run_batch_analysis():
    print(f"============================================================")
    print(f"Running PromptSec Batch Analysis for {MODEL_NAME}")
    print(f"============================================================")
    
    if not os.path.exists(BASE_DIR):
        print(f"[!] Directory '{BASE_DIR}' not found. Run setup first.")
        sys.exit(1)
        
    tasks = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
    
    full_results = {}
    csv_rows = []
    
    for task in sorted(tasks):
        task_path = os.path.join(BASE_DIR, task)
        full_results[task] = {}
        
        for var in VARIANTS:
            var_path = os.path.join(task_path, var)
            total_samples = 0
            bare_except_cnt = 0
            hardcoded_cnt = 0
            no_handling_cnt = 0
            
            if os.path.exists(var_path):
                files = [f for f in os.listdir(var_path) if f.endswith(".py")]
                for f in files:
                    file_path = os.path.join(var_path, f)
                    res = analyze_code_file(file_path)
                    total_samples += 1
                    if res["bare_except"]:
                        bare_except_cnt += 1
                    if res["hardcoded_secret"]:
                        hardcoded_cnt += 1
                    if res["no_exception_handling"]:
                        no_handling_cnt += 1
                        
            bare_pct = (bare_except_cnt / total_samples * 100) if total_samples > 0 else 0.0
            
            full_results[task][var] = {
                "total_samples": total_samples,
                "bare_except": bare_except_cnt,
                "hardcoded": hardcoded_cnt,
                "no_handling": no_handling_cnt,
                "bare_except_pct": bare_pct
            }
            
            csv_rows.append({
                "task": task,
                "variant": var,
                "total_samples": total_samples,
                "bare_except": bare_except_cnt,
                "hardcoded": hardcoded_cnt,
                "no_handling": no_handling_cnt,
                "bare_except_pct": f"{bare_pct:.2f}"
            })

    print("\nSTATISTICAL TESTING (Fisher's Exact Test vs Original):")
    if not HAS_SCIPY:
        print("[!] Note: SciPy is not installed. P-value calculations skipped.")
    
    stats_results = {}
    for task in full_results:
        stats_results[task] = {}
        orig = full_results[task].get("original", {"bare_except": 0, "total_samples": 0})
        a = orig["bare_except"]
        b = orig["total_samples"] - a
        
        for var in ["typo", "synonym", "paraphrase"]:
            curr = full_results[task].get(var, {"bare_except": 0, "total_samples": 0})
            c = curr["bare_except"]
            d = curr["total_samples"] - c
            
            p_val = None
            if HAS_SCIPY and (a + b + c + d) > 0:
                table = [[a, b], [c, d]]
                _, p_val = fisher_exact(table)
                
            stats_results[task][var] = {
                "contingency_table": [[a, b], [c, d]],
                "p_value": p_val
            }
            
            if "JWT" in task.upper():
                print(f" [⭐ JWT CRITICAL] Variant: {var:<10} | Orig Bare Except: {a}/{a+b} | Variant Bare Except: {c}/{c+d} | p-value: {p_val}")

    csv_file = f"promptsec_results_{MODEL_NAME}.csv"
    json_file = f"promptsec_results_{MODEL_NAME}.json"
    
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["task", "variant", "total_samples", "bare_except", "hardcoded", "no_handling", "bare_except_pct"])
        writer.writeheader()
        writer.writerows(csv_rows)
        
    output_json = {
        "model": MODEL_NAME,
        "metrics": full_results,
        "statistical_tests": stats_results
    }
    
    with open(json_file, "w") as f:
        json.dump(output_json, f, indent=2)
        
    print(f"\n[+] Batch analysis complete.")
    print(f"[+] CSV Export saved to: {csv_file}")
    print(f"[+] JSON Export saved to: {json_file}")

if __name__ == "__main__":
    run_batch_analysis()
