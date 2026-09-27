#!/usr/bin/env python3
"""
PromptSec Batch Sample Import & Structure Validator
Model: Gemini
"""

import os
import sys

MODEL_NAME = "Gemini"
BASE_DIR = f"generated_code_{MODEL_NAME}"
VARIANTS = ["original", "typo", "synonym", "paraphrase"]
EXPECTED_REPS = 4

def validate_samples():
    print(f"============================================================")
    print(f"PromptSec Sample Directory Validation: {MODEL_NAME}")
    print(f"============================================================")
    
    if not os.path.exists(BASE_DIR):
        print(f"[!] Error: Directory '{BASE_DIR}' does not exist. Run promptsec_direct_test.py first.")
        sys.exit(1)
        
    tasks = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
    if not tasks:
        print(f"[!] No task folders found under '{BASE_DIR}'.")
        sys.exit(1)
        
    total_found = 0
    total_expected = len(tasks) * len(VARIANTS) * EXPECTED_REPS
    
    complete_tasks = 0
    incomplete_tasks = 0
    
    for task in sorted(tasks):
        task_path = os.path.join(BASE_DIR, task)
        task_complete = True
        print(f"\nTask: {task}")
        
        for var in VARIANTS:
            var_path = os.path.join(task_path, var)
            if not os.path.exists(var_path):
                print(f"  [MISSING FOLDER] {var}")
                task_complete = False
                continue
                
            py_files = [f for f in os.listdir(var_path) if f.endswith(".py")]
            count = len(py_files)
            total_found += count
            
            status = "OK" if count == EXPECTED_REPS else f"INCOMPLETE ({count}/{EXPECTED_REPS})"
            if count != EXPECTED_REPS:
                task_complete = False
            print(f"  - {var:<12}: {count}/{EXPECTED_REPS} samples [{status}]")
            
        if task_complete:
            complete_tasks += 1
        else:
            incomplete_tasks += 1
            
    print(f"\n------------------------------------------------------------")
    print(f"VALIDATION SUMMARY:")
    print(f"Total Samples Found   : {total_found} / {total_expected}")
    print(f"Complete Tasks        : {complete_tasks}")
    print(f"Incomplete Tasks      : {incomplete_tasks}")
    print(f"Completion Percentage : {(total_found / total_expected * 100) if total_expected > 0 else 0:.1f}%")
    print(f"------------------------------------------------------------")

if __name__ == "__main__":
    validate_samples()
