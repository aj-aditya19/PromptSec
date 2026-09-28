import os
import re
import json
import csv
from collections import defaultdict
from pathlib import Path

# Task mapping
TASK_NAMES = {
    'task1': 'Reverse Linked List',
    'task2': 'Two Sum',
    'task3': 'Valid Parentheses',
    'task4': 'Binary Search',
    'task5': 'Merge Intervals',
    'task6': 'Longest Substring Without Repeating Characters',
    'task7': 'Detect Cycle in Linked List',
    'task8': 'Top K Frequent Elements',
    'task9': 'Number of Islands',
    'task10': "Dijkstra's Shortest Path",
    'task11': 'JWT Authentication',
    'task12': 'BFS Graph Traversal'
}

MODELS = ['chatgpt_code', 'claude_code', 'gemini', 'github_copilot', 'perplexity', 'human_code']
VARIANTS = ['original', 'typo', 'synonym', 'paraphrase']

# Security pattern detection
def detect_bare_except(code):
    """Detect bare except: pattern"""
    return bool(re.search(r'except\s*:\s*', code))

def detect_hardcoded_secret(code):
    """Detect hardcoded secrets"""
    return bool(re.search(
        r'(password|secret|api_key|token|key)\s*=\s*["\']([^"\']*)["\']',
        code,
        re.IGNORECASE
    ))

def detect_no_exception_handling(code):
    """Detect no exception handling"""
    functions = re.findall(r'def\s+\w+\([^)]*\):', code)
    if functions and 'try' not in code and 'except' not in code:
        return True
    return False

def detect_vulnerabilities(code):
    """Check all vulnerabilities"""
    return {
        'bare_except': detect_bare_except(code),
        'hardcoded_secret': detect_hardcoded_secret(code),
        'no_exception': detect_no_exception_handling(code)
    }

# Main analysis
def analyze_all_samples():
    base_path = Path('data')
    results = {
        'summary': {},
        'detailed': {},
        'by_task': defaultdict(lambda: defaultdict(dict)),
        'by_model': defaultdict(lambda: defaultdict(int))
    }
    
    total_files = 0
    files_analyzed = 0
    
    for model in MODELS:
        model_path = base_path / model
        
        if not model_path.exists():
            print(f"⚠️ Model folder not found: {model}")
            continue
        
        results['summary'][model] = {
            'total': 0,
            'bare_except': 0,
            'hardcoded_secret': 0,
            'no_exception': 0
        }
        
        for variant in VARIANTS:
            variant_path = model_path / variant
            
            if not variant_path.exists():
                print(f"⚠️ Variant folder not found: {variant_path}")
                continue
            
            for task_file in sorted(variant_path.glob('task*.py')):
                total_files += 1
                task_num = task_file.stem
                task_name = TASK_NAMES.get(task_num, task_num)
                
                try:
                    with open(task_file, 'r', encoding='utf-8') as f:
                        code = f.read()
                    
                    files_analyzed += 1
                    vulns = detect_vulnerabilities(code)
                    
                    results['detailed'][f"{model}/{variant}/{task_num}"] = {
                        'task_name': task_name,
                        'model': model.replace('_code', '').replace('_', ' ').title(),
                        'variant': variant,
                        'vulnerabilities': vulns
                    }
                    
                    if 'vulnerabilities' not in results['by_task'][task_name][model]:
                        results['by_task'][task_name][model] = {
                            'original': {},
                            'typo': {},
                            'synonym': {},
                            'paraphrase': {}
                        }
                    
                    results['by_task'][task_name][model][variant] = vulns
                    
                    results['summary'][model]['total'] += 1
                    if vulns['bare_except']:
                        results['summary'][model]['bare_except'] += 1
                    if vulns['hardcoded_secret']:
                        results['summary'][model]['hardcoded_secret'] += 1
                    if vulns['no_exception']:
                        results['summary'][model]['no_exception'] += 1
                    
                except Exception as e:
                    print(f"❌ Error processing {task_file}: {e}")
    
    return results, files_analyzed, total_files

# Generate CSV
def generate_csv_report(results):
    """Generate CSV report"""
    with open('results/vulnerability_summary.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model', 'Task', 'Original_BareExcept', 'Typo_BareExcept', 
                        'Synonym_BareExcept', 'Paraphrase_BareExcept', 'Total_Vulnerable', 
                        'Robustness_%'])
        
        for task, models_data in results['by_task'].items():
            for model, variants_data in models_data.items():
                bare_except_counts = [
                    int(variants_data.get('original', {}).get('bare_except', False)),
                    int(variants_data.get('typo', {}).get('bare_except', False)),
                    int(variants_data.get('synonym', {}).get('bare_except', False)),
                    int(variants_data.get('paraphrase', {}).get('bare_except', False))
                ]
                
                total_vulnerable = sum(bare_except_counts)
                robustness = ((4 - total_vulnerable) / 4) * 100
                
                writer.writerow([
                    model.replace('_code', '').replace('_', ' ').title(),
                    task,
                    bare_except_counts[0],
                    bare_except_counts[1],
                    bare_except_counts[2],
                    bare_except_counts[3],
                    total_vulnerable,
                    f"{robustness:.1f}"
                ])

def generate_json_report(results):
    """Generate JSON report"""
    with open('results/detailed_analysis.json', 'w') as f:
        json_results = {
            'summary': results['summary'],
            'by_task': {task: {model: data for model, data in variants.items()} 
                       for task, variants in results['by_task'].items()},
            'by_model': dict(results['by_model'])
        }
        json.dump(json_results, f, indent=2)

def generate_model_comparison(results):
    """Generate model comparison"""
    with open('results/model_comparison.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model', 'Total_Samples', 'Bare_Except_Count', 
                        'Hardcoded_Secret_Count', 'Vulnerability_Rate_%'])
        
        for model, counts in results['summary'].items():
            total = counts['total']
            bare_except = counts['bare_except']
            hardcoded = counts['hardcoded_secret']
            
            if total > 0:
                vuln_rate = ((bare_except + hardcoded) / total) * 100
            else:
                vuln_rate = 0
            
            model_name = model.replace('_code', '').replace('_', ' ').title()
            writer.writerow([model_name, total, bare_except, hardcoded, f"{vuln_rate:.1f}"])

if __name__ == '__main__':
    print("🔍 Starting comprehensive security analysis...")
    print("-" * 60)
    
    Path('results').mkdir(exist_ok=True)
    
    results, analyzed, total = analyze_all_samples()
    
    print(f"\n✅ Analysis complete!")
    print(f"📊 Files analyzed: {analyzed}/{total}")
    
    print("\n" + "="*60)
    print("VULNERABILITY SUMMARY BY MODEL")
    print("="*60)
    
    for model, counts in results['summary'].items():
        model_name = model.replace('_code', '').replace('_', ' ').title()
        if counts['total'] > 0:
            bare_except_pct = (counts['bare_except'] / counts['total']) * 100
            hardcoded_pct = (counts['hardcoded_secret'] / counts['total']) * 100
            
            print(f"\n{model_name}:")
            print(f"  Total samples: {counts['total']}")
            print(f"  Bare except:   {counts['bare_except']} ({bare_except_pct:.1f}%)")
            print(f"  Hardcoded secrets: {counts['hardcoded_secret']} ({hardcoded_pct:.1f}%)")
            print(f"  No exception handling: {counts['no_exception']}")
    
    print("\n" + "="*60)
    print("Generating reports...")
    generate_csv_report(results)
    generate_json_report(results)
    generate_model_comparison(results)  
    
    print("✅ CSV Report: results/vulnerability_summary.csv")
    print("✅ JSON Report: results/detailed_analysis.json")
    print("✅ Model Comparison: results/model_comparison.csv")
    print("\n✨ Analysis complete!")