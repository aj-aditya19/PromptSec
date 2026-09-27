# PromptSec Phase 2 — Quickstart

## 1. Prerequisites

Python 3.9+ is recommended.

Optional packages:
```bash
python -m pip install scipy
python -m pip install bandit
```

The main analyzer runs without SciPy, but Fisher's exact p-values require SciPy.
The optional security scanner requires Bandit.

## 2. Prepare the model output directory

The package already contains the required directory template:

```text
generated_code_ChatGPT/
  Reverse Linked List/
    original/rep_1.py ... rep_4.py
    typo/rep_1.py ... rep_4.py
    synonym/rep_1.py ... rep_4.py
    paraphrase/rep_1.py ... rep_4.py
  ...
```

The same structure exists for all 12 tasks.

## 3. Generate samples

Open TESTING_CHECKLIST.md and use each prompt exactly as written.

For each variant:
- generate four independent samples;
- label them rep_1 through rep_4;
- save the generated Python code only;
- do not include Markdown fences such as ```python in the saved file;
- do not manually fix generated code before analysis.

If a model returns explanatory text, save the code portion that was generated.
Keep any raw transcript separately if your research protocol requires it.

## 4. Validate

From the framework directory:

```bash
python promptsec_import_samples.py
```

For a specific root:

```bash
python promptsec_import_samples.py --root generated_code_ChatGPT
```

The validator reports complete and incomplete task/variant groups.

## 5. Analyze

Run:

```bash
python promptsec_batch_analyzer.py
```

Or:

```bash
python promptsec_batch_analyzer.py --root generated_code_ChatGPT --output analysis_results
```

Outputs:
- `analysis_results/security_summary.csv`
- `analysis_results/security_results.json`
- `analysis_results/fisher_tests.csv`

The Fisher comparisons are:
- Original vs Typo
- Original vs Synonym
- Original vs Paraphrase

A p-value below 0.05 is reported as statistically significant under the
specified threshold. Statistical significance is not itself a measure of
practical security severity.

## 6. Optional Bandit analysis

```bash
python promptsec_security_analysis.py --root generated_code_ChatGPT --output bandit_results
```

This creates a JSON report containing Bandit findings where Bandit is installed.

## 7. Recreate the directory template

If you need a fresh model directory:

```bash
python promptsec_direct_test.py --model ChatGPT
```

This creates all 12 task directories and all 192 expected file paths.

## 8. Research hygiene

Do not:
- change prompt wording during collection;
- replace a failed generation with a manually authored solution;
- delete insecure outputs;
- mix outputs from different models;
- change variant labels after collection.

Do:
- retain all outputs;
- record model name/version and collection date separately;
- keep the four repetitions independent;
- run validation before analysis.
