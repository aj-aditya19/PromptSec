#!/usr/bin/env python3
"""
PromptSec Phase 2 Framework Initialization & Directory Setup
Model: Gemini
"""

import os
import sys

MODEL_NAME = "Gemini"
BASE_DIR = f"generated_code_{MODEL_NAME}"

TASKS = [
    "1. Reverse Linked List",
    "2. Two Sum",
    "3. Valid Parentheses",
    "4. Binary Search",
    "5. Merge Intervals",
    "6. Longest Substring Without Repeating Characters",
    "7. Detect Cycle in Linked List",
    "8. Top K Frequent Elements",
    "9. Number of Islands",
    "10. Dijkstras Shortest Path",
    "11. JWT Authentication",
    "12. BFS Graph Traversal"
]

VARIANTS = ["original", "typo", "synonym", "paraphrase"]

def setup_framework():
    print(f"[*] Initializing PromptSec Framework structure for {MODEL_NAME}...")
    os.makedirs(BASE_DIR, exist_ok=True)
    
    total_dirs = 0
    for task in TASKS:
        for var in VARIANTS:
            path = os.path.join(BASE_DIR, task, var)
            os.makedirs(path, exist_ok=True)
            total_dirs += 1
            
    print(f"[+] Successfully verified/created {total_dirs} target sample directories in '{BASE_DIR}'.")
    print("[+] PromptSec Phase 2 direct test setup complete.")

if __name__ == "__main__":
    setup_framework()
