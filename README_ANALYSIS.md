# What was done (steps) and how to rerun

## Steps performed
1. **Received** `promptsec.zip` (5 models x 4 variants x 20 tasks = 400 files, empty `Human-Code/`, `metadata.csv`).
2. **Checked the data**: 400 files present, none empty, every file defines the function name required by its task
   (`ast` check), 399/400 parse. `Gemini/typo/task18.py` did not parse (copy turned `"\n"` into a real newline).
3. **Cleaned a copy** (`Data_clean/`): removed `__pycache__` and a stray `requirements.txt`, renamed
   `Claude/orginal` -> `original`, `GitHub-Copilot` -> `Copilot`, restored the escapes in Gemini/typo/task18. See `data_fixes.md`.
4. **Wrote the rules first** (`RULES.md`): for each of the 20 tasks, what counts as "vulnerable", before running any test on the data.
5. **Installed tools**: Bandit, PyJWT, PyYAML, requests, cryptography, lxml, defusedxml, psycopg2, bcrypt, scipy, pandas.
   Semgrep installed but its rule registry could not be downloaded in the sandbox, so Semgrep was NOT used.
6. **Wrote the test harness** (`harness.py`): one test per task. It imports the generated file and calls the required function
   with (a) normal input (functional test) and (b) attack inputs or static checks (security test).
7. **Wrote the runner** (`run_all.py`): runs every file in its own subprocess, temp folder, 40 s timeout, CPU/memory/file-size limits,
   fake `ping`, no real network. Then runs Bandit on every folder and merges the results.
8. **Validated the tests with controls** (`controls/`): 20 deliberately vulnerable and 20 safe reference samples.
   Result: 20/20 vulnerable detected, 0/20 safe flagged (`controls.csv`). Fixed two test problems found in the first smoke test
   (task 11 localhost blocked by SSRF protection = "not testable"; task 19 needed more DB environment variables).
9. **Ran all 400 files** -> `per_file.csv`.
10. **Analysed** (`analyze.py` -> `summary.txt`): counts per model x variant, per task, flag types, functional rates,
    McNemar exact tests (variant vs original, paired by model+task), Holm correction.
11. **Looked at the odd result** (Gemini original 9 vs typo 0) by reading a few files: the typo chat wrote more defensive code.

## Files
| File | What it is |
|---|---|
| `RULES.md` | pre-registered vulnerability rules for the 20 tasks |
| `data_fixes.md` | every change made to the data |
| `harness.py` | the 20 tests (attack / static checks) |
| `run_all.py` | runs all files + Bandit, writes `results/per_file.csv` |
| `analyze.py` | tables and statistics, writes `results/summary.txt` |
| `controls/` | 20 vulnerable + 20 safe control samples for validating the tests |
| `Data_clean/` | the cleaned 400 files used for the analysis |
| `results/per_file.csv` | one row per file: functional, vulnerable, flags, Bandit ids |
| `results/summary.txt` | all tables and p-values |
| `results/controls.csv` | test results on the control samples |

## Rerun
```bash
pip install bandit pyjwt pyyaml requests cryptography lxml defusedxml psycopg2-binary bcrypt argon2-cffi passlib scipy pandas
python3 run_all.py        # runs 400 files + Bandit  (about 1-2 minutes)
python3 analyze.py        # tables + McNemar tests
# validate the tests on the controls:
PS_ROOT=controls PS_MODELS=vuln,safe PS_VARIANTS=x PS_OUT=results/controls.csv python3 run_all.py
```
Run generated code only inside a sandbox or container.

## Limitations (keep in the paper)
- One chat per model x variant (all 20 tasks in that chat): variant effects cannot be separated from chat-to-chat randomness.
  The McNemar tests treat the 100 (model, task) pairs as independent, which they are not. Use them as exploratory only.
- Bandit-only flags (task 9: `xml.etree` B314/B405, 10 files) were not confirmed by the XXE attack test; both numbers are reported.
- Task 11 "no timeout" and task 14 timing checks are static checks. Task 11 SSRF is recorded as info only.
- Semgrep was not used. Static + attack tests do not cover every weakness.
- Human baseline not analysed yet (`Human-Code/` empty). Model versions are as typed in `metadata.csv`.
- The analyst/test writer (Claude Sonnet 5.5) is also one of the 5 models tested; the rules in `RULES.md` are public so others can check them.
