# PromptSec Phase 2 Quickstart Guide (Gemini)

This document outlines the step-by-step process for executing PromptSec Phase 2 evaluations on **Gemini**.

---

## Step 1: Framework Setup
Ensure you have Python 3 and required dependencies installed:
```bash
pip install scipy bandit
```

Verify directory structure:
```bash
python3 promptsec_direct_test.py
```

---

## Step 2: Sampling Process
1. Open `TESTING_CHECKLIST.md`.
2. For each task (1 to 12) and each variant (`original`, `typo`, `synonym`, `paraphrase`):
   - Submit the prompt to **Gemini** 4 separate times in new/fresh sessions.
   - Save the raw Python response into:
     `generated_code_Gemini/<Task_Name>/<variant>/rep_<1-4>.py`

---

## Step 3: Validate Sample Collection
Run the validation script to check missing or incomplete task samples:
```bash
python3 promptsec_import_samples.py
```
This script ensures all 192 samples are present before running statistical tests.

---

## Step 4: Run Security & Statistical Analysis
Execute the main batch analyzer:
```bash
python3 promptsec_batch_analyzer.py
```

Outputs generated:
- `promptsec_results_Gemini.csv`: Tabular summary of anti-patterns across variants.
- `promptsec_results_Gemini.json`: Full analysis output including Fisher's exact test p-values.

---

## Step 5: Optional Deep Scanning
For deeper Static Application Security Testing (SAST):
```bash
python3 promptsec_security_analysis.py
```
This leverages `Bandit` alongside custom AST and regex patterns.
