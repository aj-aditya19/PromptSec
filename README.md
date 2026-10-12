# PromptSec: Does prompt wording change the security of AI-generated code?

## Research question
Do small changes in how a coding prompt is worded (typos, synonyms, paraphrase) change the security of the code an AI tool writes?

## Design
- **20 security-related Python tasks** (SQL query, path traversal x2, command injection, password hashing, reset token, OTP, JWT,
  XML, YAML, URL fetch, encryption, HTML output, token compare, temp file, zip, redirect, logging, DB credentials, secret file).
- **4 prompt variants** per task: `original`, `typo`, `synonym`, `paraphrase` (the function signature line is identical in all variants).
- **5 AI tools:** Claude, ChatGPT, Gemini, GitHub Copilot, Perplexity. One chat per tool x variant, all 20 tasks in that chat
  (400 files, one sample per cell). No repeats were collected.
- Comparison: each variant against `original`, paired by (tool, task).

## How it was tested
`RULES.md` (written before running any test) defines what counts as vulnerable for each task.
`harness.py` runs normal-input and attack tests in a sandboxed subprocess (temp folder, timeout, resource limits); `run_all.py`
adds Bandit. The tests were validated on 20 vulnerable + 20 safe control samples (`controls/`): all detected, none falsely flagged.
Semgrep was not used (its rules could not be downloaded in the sandbox).
"Confirmed" = a test of ours proved the weakness. "Combined" = confirmed OR a Bandit finding with the task's CWE (medium+).

## Results (vulnerable files; 20 per cell)
Confirmed by test:

| Model | original | typo | synonym | paraphrase | total |
|---|---|---|---|---|---|
| Claude | 0 | 0 | 0 | 0 | 0 |
| ChatGPT | 0 | 1 | 0 | 0 | 1 |
| Copilot | 1 | 0 | 1 | 0 | 2 |
| Perplexity | 2 | 0 | 2 | 3 | 7 |
| Gemini | 8 | 0 | 3 | 4 | 15 |
| **All** | 11 | 1 | 6 | 7 | **25 / 400 (6%)** |

- Combined rule: 35/400 files (the extra 10 are Bandit-only `xml.etree` flags in task 9, not confirmed by the XXE attack).
- Most common confirmed problems: log injection (8 files), open redirect (5), hardcoded JWT secret (5).
- All tested files passed the functional tests (8 files were not testable because they block localhost).
- **Does wording matter?** In this pilot, yes for some tools, but not in the expected direction. Typo prompts gave FEWER confirmed
  vulnerabilities than original (11 -> 1; McNemar exact, Holm-corrected p = 0.019), mostly Gemini (8 -> 0). Synonym (11 -> 6) and
  paraphrase (11 -> 7) were not significant after correction (p = 0.25). Claude, ChatGPT and Copilot showed almost no vulnerabilities
  in any variant, so there was little to change.

## Limitations (must be in the paper)
1. One chat per model x variant, so a variant effect cannot be separated from chat-to-chat randomness. The 20 tasks of one chat are not
   independent; the McNemar p-values treat them as independent and are optimistic. Treat results as exploratory.
2. Most of the effect comes from one tool (Gemini); the other tools are near zero (floor effect).
3. Tests, rules and analysis were written by Claude Sonnet 5.5, which is also one of the 5 tested tools. Rules are public in `RULES.md`.
4. Static and attack tests do not cover every weakness; Semgrep not used; task 11 (no timeout) and task 14 (timing) are static checks.
5. Model versions and dates are as typed in `metadata.csv`; models change over time.

## Rerun
```bash
pip install -r requirements.txt
python3 make_data_clean.py     # builds Data_clean/ from Data/ (fixes listed in data_fixes.md)
python3 run_all.py             # runs the 400 files + Bandit -> results/per_file.csv
python3 analyze.py             # tables and McNemar tests -> results/summary.txt
```
Run generated code only inside a sandbox or container.

## Files
`Data/` raw files as collected | `make_data_clean.py` builds `Data_clean/` | `metadata.csv` model, version, date, interface per chat |
`prompts/` the 4 batch prompts used | `RULES.md` rules | `data_fixes.md` data changes | `harness.py` tests | `run_all.py` runner |
`analyze.py` statistics | `controls/` validation samples | `results/` all outputs
