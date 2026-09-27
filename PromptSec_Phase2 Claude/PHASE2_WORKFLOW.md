# PromptSec Phase 2: Complete Testing Workflow

## Overview

This phase extends the research to **all 12 tasks with n=4 repetitions** across Claude and compares with baseline data from ChatGPT, Gemini, Copilot, and Perplexity.

**Status:** Framework ready ✅
**Framework Created:** 2026-09-27

---

## Step 1: Generate Code Samples (ONGOING)

### What to do:
Test Claude on **all 192 prompts** (12 tasks × 4 variants × 4 repetitions)

### Prompt Source:
See `/home/claude/TESTING_CHECKLIST.md` for all exact prompts

### For each prompt:
1. Copy the prompt from the checklist
2. Ask Claude to generate the code
3. Save output to: `/home/claude/generated_code/{TASK}/{VARIANT}/rep_{N}.py`

### Directory Structure:
```
/home/claude/generated_code/
├── Reverse Linked List/
│   ├── original/
│   │   ├── rep_1.py
│   │   ├── rep_2.py
│   │   ├── rep_3.py
│   │   └── rep_4.py
│   ├── typo/
│   ├── synonym/
│   └── paraphrase/
├── Two Sum/
│   ├── original/
│   ├── typo/
│   ├── synonym/
│   └── paraphrase/
... (12 tasks total)
```

### Naming Convention:
- **TASK names** (folder names): Exact from Phase 1 metadata
- **VARIANT names**: `original`, `typo`, `synonym`, `paraphrase`
- **FILE names**: `rep_1.py`, `rep_2.py`, `rep_3.py`, `rep_4.py`

---

## Step 2: Security Analysis (AUTOMATED)

### What happens:
Once samples are collected, run:
```bash
python3 /home/claude/promptsec_batch_analyzer.py
```

### What it checks:
- ✓ Bare `except:` pattern (security anti-pattern)
- ✓ Hardcoded secrets/credentials
- ✓ No exception handling
- ✓ Fisher's exact test (original vs variant)

### Output Files:
- `/home/claude/promptsec_summary.csv` — summary table
- `/home/claude/promptsec_batch_results.json` — detailed results
- Console output with p-values for each variant

---

## Step 3: Statistical Testing

### Fisher's Exact Test (Automated)

Tests the hypothesis: **Does prompt perturbation increase code vulnerabilities?**

For JWT Authentication task:
- **Contingency table:** 2×2 (safe/unsafe × original/variant)
- **Null hypothesis:** No difference in unsafe code rate
- **Significance threshold:** p < 0.05

### Test Comparisons:
- Original vs Typo
- Original vs Synonym  
- Original vs Paraphrase
- Original vs Combined (Synonym + Paraphrase)

### Expected Output Format:
```
Variant vs ORIGINAL:
  Unsafe: 3/4 vs 0/4
  p-value: 0.0286 ✓ SIGNIFICANT
```

---

## Step 4: Merge with Baseline Data

### Existing Data (Already Collected):
- ChatGPT (n=4 per variant) ✅
- Gemini (n=4 per variant) ✅
- GitHub Copilot (n=4 per variant) ✅
- Perplexity (n=4 per variant) ✅
- Claude (n=4 per variant) — IN PROGRESS

### Merge Process:
Once Claude n=4 is ready:
1. Load all 5 models' JWT data
2. Run combined Fisher's test
3. Calculate effect sizes (odds ratios)
4. Create comparative tables and visualizations

---

## Step 5: Paper Write-Up

### Sections to Update:

#### Results Section:
- Add **Claude n=4 findings** alongside baseline models
- Include **per-variant comparison table** (all 5 models)
- Add **statistical significance column** (p-values)

#### Key Results to Report:
1. Security sensitivity by model (JWT focus)
2. Perturbation type effect (typo/synonym/paraphrase)
3. Functional correctness across all 5 models
4. Consistency metrics (repetition stability)

#### Figures to Generate:
- **Figure 1 (Security):** Bar chart with p-values (5 models × 4 variants)
- **Figure 2 (Heatmap):** Risk matrix (models vs perturbations)
- **Figure 3 (Functional):** Correctness across all 5 models
- **Figure 4 (Stability):** Variance in n=4 repetitions

---

## File Reference

### Python Scripts Created:

| Script | Purpose |
|--------|---------|
| `promptsec_direct_test.py` | Setup framework & generate testing guide |
| `promptsec_batch_analyzer.py` | Security analysis & Fisher's exact test |
| `promptsec_security_analysis.py` | Detailed Bandit scanning (optional) |

### Data Files:

| File | Purpose |
|------|---------|
| `TESTING_CHECKLIST.md` | All 192 prompts organized by task |
| `PHASE2_WORKFLOW.md` | This file - complete workflow |
| `generated_code/{...}` | Collected code samples |
| `promptsec_batch_results.json` | Full analysis results |
| `promptsec_summary.csv` | Summary statistics |

---

## Timeline

| Phase | Task | Status |
|-------|------|--------|
| **Framework** | Scripts & structure ready | ✅ Done |
| **Collection** | Generate all 192 samples | 🔄 IN PROGRESS |
| **Analysis** | Security scanning & Fisher test | ⏳ Pending samples |
| **Merge** | Combine with 4 model baseline | ⏳ Pending Claude data |
| **Paper** | Update Results + Discussion + Conclusion | ⏳ Pending analysis |

---

## Success Criteria

- [✅] Framework scripts created
- [ ] All 192 Claude samples collected
- [ ] Security analysis runs without errors
- [ ] Fisher's test p-values calculated
- [ ] All 5 models' results merged
- [ ] Paper Results section updated
- [ ] All figures regenerated
- [ ] Final paper draft complete

---

## Usage

### Run Analysis (once samples are collected):
```bash
cd /home/claude
python3 promptsec_batch_analyzer.py
```

### View Results:
```bash
cat promptsec_summary.csv
cat promptsec_batch_results.json | python3 -m json.tool
```

---

## Notes for Aditya

- **n=4 requirement:** All variants must have exactly 4 samples
- **File naming:** Strict naming required for parser to work
- **Critical task:** JWT Authentication — watch for `bare except:` pattern
- **Variants matter:** Typo smallest effect, Paraphrase strongest (hypothesis)
- **Statistical power:** With n=4, Fisher test is underpowered but provides direction

---

**Created:** 2026-09-27
**Framework Status:** ✅ Ready
**Next Step:** Collect all 192 Claude samples
