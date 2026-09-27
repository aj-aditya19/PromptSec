# PromptSec Phase 2 Quickstart

## 1. Collect samples

Test GitHub Copilot using each prompt in `TESTING_CHECKLIST.md`. For every task and variant, request four independent answers. Save only the generated Python code in:

`<Task>/<variant>/rep_1.py` through `rep_4.py`

Keep the model, temperature/settings, system context, and collection procedure consistent. Do not silently repair generated code before analysis.

## 2. Validate the dataset

From this folder run:

```powershell
python promptsec_import_samples.py
```

The expected result is 192 Python files: 12 tasks, 4 variants, and 4 repetitions each.

## 3. Analyze security indicators

```powershell
python promptsec_batch_analyzer.py
```

Outputs are placed in `analysis_output/`:

- `security_summary.csv`
- `security_results.json`
- `fisher_tests.csv`

The analyzer checks bare `except`, likely hardcoded secrets, and absence of `try`/`except` handling. These are screening indicators, not proof of exploitability.

## 4. Run deeper checks

```powershell
python promptsec_security_analysis.py
```

Install optional dependencies when needed:

```powershell
python -m pip install bandit scipy
```

## 5. Preserve research integrity

Record collection date, model version, settings, prompt variant, repetition number, and any refusal or non-Python answer. Keep raw responses separately if your protocol permits. Report missing samples rather than replacing them with invented data.

## Expected layout

```text
PromptSec_Phase2 Github_Copliot/
  Reverse Linked List/original/rep_1.py ... rep_4.py
  ...
  JWT Authentication/original/rep_1.py ... rep_4.py
  analysis_output/
```
