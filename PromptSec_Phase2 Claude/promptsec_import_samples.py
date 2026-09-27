#!/usr/bin/env python3
"""
PromptSec Sample Import Utility
Batch import code samples from various formats into the proper directory structure
"""

import json
import os
from pathlib import Path

def import_from_json(json_file):
    """Import samples from a JSON file with structure: {task: {variant: [code1, code2, ...]}"""
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return False
    
    base_path = Path("/home/claude/generated_code")
    imported_count = 0
    
    for task_name, variants in data.items():
        if not isinstance(variants, dict):
            continue
        
        for variant_name, samples in variants.items():
            if not isinstance(samples, list):
                continue
            
            task_dir = base_path / task_name / variant_name
            task_dir.mkdir(parents=True, exist_ok=True)
            
            for idx, code in enumerate(samples, 1):
                if not code or not isinstance(code, str):
                    continue
                
                file_path = task_dir / f"rep_{idx}.py"
                
                try:
                    with open(file_path, 'w') as f:
                        f.write(code)
                    imported_count += 1
                except Exception as e:
                    print(f"Error writing {file_path}: {e}")
    
    print(f"✓ Imported {imported_count} samples from JSON")
    return True

def import_from_text_files(source_dir):
    """Import samples from a directory of .txt or .py files with naming convention:
    
    Expected structure:
    source_dir/
    ├── Reverse Linked List_original_1.txt
    ├── Reverse Linked List_original_2.txt
    ├── Reverse Linked List_typo_1.txt
    ...
    """
    
    source_path = Path(source_dir)
    if not source_path.exists():
        print(f"Source directory not found: {source_dir}")
        return False
    
    base_path = Path("/home/claude/generated_code")
    imported_count = 0
    
    for file_path in source_path.glob("*"):
        if not file_path.is_file():
            continue
        
        # Parse filename: TASK_NAME_variant_rep_number
        name = file_path.stem
        parts = name.rsplit('_', 2)  # Split from right: [task_variant, variant, rep_num]
        
        if len(parts) < 3:
            print(f"Skipping {file_path.name} - invalid naming convention")
            continue
        
        # Reconstruct task and variant
        task_name = "_".join(parts[:-2])
        variant_name = parts[-2]
        rep_num = parts[-1]
        
        try:
            rep_num = int(rep_num)
        except:
            print(f"Skipping {file_path.name} - invalid repetition number")
            continue
        
        # Read source file
        try:
            with open(file_path, 'r') as f:
                code = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        
        # Write to target location
        task_dir = base_path / task_name / variant_name
        task_dir.mkdir(parents=True, exist_ok=True)
        
        target_file = task_dir / f"rep_{rep_num}.py"
        
        try:
            with open(target_file, 'w') as f:
                f.write(code)
            imported_count += 1
            print(f"✓ {task_name}/{variant_name}/rep_{rep_num}")
        except Exception as e:
            print(f"Error writing {target_file}: {e}")
    
    print(f"\n✓ Imported {imported_count} samples from text files")
    return True

def validate_structure():
    """Validate that all required directories have n=4 samples"""
    
    base_path = Path("/home/claude/generated_code")
    if not base_path.exists():
        print("Generated code directory not found")
        return False
    
    total_tasks = 0
    complete_tasks = 0
    missing_samples = []
    
    tasks = [d for d in base_path.iterdir() if d.is_dir()]
    
    for task_dir in sorted(tasks):
        total_tasks += 1
        task_complete = True
        
        for variant in ["original", "typo", "synonym", "paraphrase"]:
            variant_dir = task_dir / variant
            
            if not variant_dir.exists():
                missing_samples.append(f"{task_dir.name}/{variant}: directory missing")
                task_complete = False
                continue
            
            # Count .py files
            py_files = list(variant_dir.glob("rep_*.py"))
            
            if len(py_files) < 4:
                missing_samples.append(f"{task_dir.name}/{variant}: only {len(py_files)}/4 samples")
                task_complete = False
        
        if task_complete:
            complete_tasks += 1
            print(f"✓ {task_dir.name:45} [COMPLETE]")
        else:
            print(f"✗ {task_dir.name:45} [INCOMPLETE]")
    
    print(f"\n{'='*70}")
    print(f"Task Status: {complete_tasks}/{total_tasks} tasks complete")
    print(f"{'='*70}")
    
    if missing_samples:
        print(f"\nMissing samples:")
        for missing in missing_samples[:10]:
            print(f"  - {missing}")
        if len(missing_samples) > 10:
            print(f"  ... and {len(missing_samples) - 10} more")
    
    return complete_tasks == total_tasks

def main():
    import sys
    
    print("=" * 70)
    print("PromptSec Sample Import Utility")
    print("=" * 70)
    
    if len(sys.argv) > 1:
        source = sys.argv[1]
        
        if source.endswith('.json'):
            print(f"\nImporting from JSON: {source}")
            import_from_json(source)
        elif os.path.isdir(source):
            print(f"\nImporting from directory: {source}")
            import_from_text_files(source)
        else:
            print(f"Unknown source: {source}")
    else:
        print("\nUsage:")
        print("  python3 promptsec_import_samples.py <json_file>")
        print("  python3 promptsec_import_samples.py <directory>")
        print("\nOr for validation only:")
    
    # Always run validation
    print("\nValidating existing structure...")
    validate_structure()

if __name__ == "__main__":
    main()
