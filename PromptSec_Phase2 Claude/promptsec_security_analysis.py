#!/usr/bin/env python3
"""
PromptSec Security Analysis - Bandit scanning and exception pattern detection
"""

import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

def check_bare_except(code):
    """Check for bare except: pattern (security anti-pattern)"""
    # Match bare except without exception specification
    pattern = r'except\s*:'
    return bool(re.search(pattern, code))

def check_hardcoded_secrets(code):
    """Check for hardcoded credentials, tokens, secrets"""
    secret_patterns = [
        r"secret\s*=\s*['\"]([^'\"]+)['\"]",
        r"password\s*=\s*['\"]([^'\"]+)['\"]",
        r"api_key\s*=\s*['\"]([^'\"]+)['\"]",
        r"token\s*=\s*['\"]([^'\"]+)['\"]",
        r"aws_secret\s*=\s*['\"]([^'\"]+)['\"]",
    ]
    
    for pattern in secret_patterns:
        if re.search(pattern, code, re.IGNORECASE):
            return True
    return False

def check_no_exception_handling(code):
    """Check if code has no try-except blocks at all"""
    return 'try:' not in code

def run_bandit(code_snippet):
    """Run Bandit security scanner on code"""
    try:
        # Write code to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code_snippet)
            temp_file = f.name
        
        # Run Bandit
        result = subprocess.run(
            ['bandit', '-f', 'json', temp_file],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Parse results
        if result.stdout:
            bandit_results = json.loads(result.stdout)
            return {
                "issues_found": len(bandit_results.get("results", [])),
                "severity_levels": {r["severity"]: r["test_id"] for r in bandit_results.get("results", [])},
                "details": bandit_results.get("results", [])
            }
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Clean up
        if 'temp_file' in locals():
            try:
                os.unlink(temp_file)
            except:
                pass
    
    return {"issues_found": 0}

def analyze_security(raw_results_file, output_file):
    """Analyze security of all generated code"""
    
    with open(raw_results_file, 'r') as f:
        raw_data = json.load(f)
    
    security_analysis = {
        "timestamp": raw_data["metadata"]["timestamp"],
        "model": raw_data["metadata"]["model"],
        "analysis_date": str(Path(raw_results_file).stat().st_mtime),
        "security_findings": {}
    }
    
    total_samples = 0
    samples_with_bare_except = 0
    samples_with_hardcoded = 0
    samples_with_no_handling = 0
    samples_with_bandit_issues = 0
    
    for task_name, task_data in raw_data["results"].items():
        print(f"\nAnalyzing: {task_name}")
        task_security = {}
        
        for variant_name, variant_data in task_data.items():
            variant_security = {
                "bare_except_samples": 0,
                "hardcoded_secrets_samples": 0,
                "no_exception_handling": 0,
                "bandit_issues_samples": 0,
                "details": []
            }
            
            for rep_data in variant_data:
                total_samples += 1
                code = rep_data["code"]
                
                if not code:
                    continue
                
                # Check for security patterns
                has_bare_except = check_bare_except(code)
                has_hardcoded = check_hardcoded_secrets(code)
                no_exception = check_no_exception_handling(code)
                
                if has_bare_except:
                    samples_with_bare_except += 1
                if has_hardcoded:
                    samples_with_hardcoded += 1
                if no_exception:
                    samples_with_no_handling += 1
                
                # Run Bandit (lightweight - only on critical tasks)
                if task_name in ["JWT Authentication", "BFS Graph Traversal"]:
                    bandit_results = run_bandit(code)
                    if bandit_results.get("issues_found", 0) > 0:
                        samples_with_bandit_issues += 1
                else:
                    bandit_results = {"skipped": "task_not_critical"}
                
                variant_security["details"].append({
                    "repetition": rep_data["repetition"],
                    "bare_except": has_bare_except,
                    "hardcoded_secrets": has_hardcoded,
                    "no_exception_handling": no_exception,
                    "bandit": bandit_results
                })
                
                if has_bare_except:
                    variant_security["bare_except_samples"] += 1
                if has_hardcoded:
                    variant_security["hardcoded_secrets_samples"] += 1
                if no_exception:
                    variant_security["no_exception_handling"] += 1
            
            task_security[variant_name] = variant_security
            
            print(f"  {variant_name:15} - bare_except: {variant_security['bare_except_samples']}/4, "
                  f"hardcoded: {variant_security['hardcoded_secrets_samples']}/4, "
                  f"no_handling: {variant_security['no_exception_handling']}/4")
        
        security_analysis["security_findings"][task_name] = task_security
    
    # Summary statistics
    security_analysis["summary"] = {
        "total_samples_analyzed": total_samples,
        "bare_except_total": samples_with_bare_except,
        "hardcoded_secrets_total": samples_with_hardcoded,
        "no_exception_handling_total": samples_with_no_handling,
        "bandit_issues_total": samples_with_bandit_issues,
        "percentages": {
            "bare_except_pct": round(samples_with_bare_except / total_samples * 100, 2) if total_samples > 0 else 0,
            "hardcoded_pct": round(samples_with_hardcoded / total_samples * 100, 2) if total_samples > 0 else 0,
            "no_handling_pct": round(samples_with_no_handling / total_samples * 100, 2) if total_samples > 0 else 0,
        }
    }
    
    # Save analysis
    with open(output_file, 'w') as f:
        json.dump(security_analysis, f, indent=2)
    
    print("\n" + "=" * 70)
    print("SECURITY ANALYSIS SUMMARY")
    print("=" * 70)
    print(f"Total samples: {total_samples}")
    print(f"Bare except instances: {samples_with_bare_except} ({security_analysis['summary']['percentages']['bare_except_pct']}%)")
    print(f"Hardcoded secrets: {samples_with_hardcoded} ({security_analysis['summary']['percentages']['hardcoded_pct']}%)")
    print(f"No exception handling: {samples_with_no_handling} ({security_analysis['summary']['percentages']['no_handling_pct']}%)")
    print(f"\nResults saved to: {output_file}")
    print("=" * 70)

if __name__ == "__main__":
    raw_file = "/home/claude/claude_testing_raw_n4.json"
    output_file = "/home/claude/claude_security_analysis_n4.json"
    
    print("Starting security analysis...")
    analyze_security(raw_file, output_file)
