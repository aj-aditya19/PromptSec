# PromptSec Phase 2 Reference

## Research question

Does prompt perturbation affect the security of AI-generated code?

The experiment compares original prompts with typo, synonym, and paraphrase variants across 12 coding tasks. Each cell has four independent repetitions. The expected dataset size is 192 samples.

## Repository layout

Each task directory contains `original`, `typo`, `synonym`, and `paraphrase`. Each variant should contain `rep_1.py` through `rep_4.py`. `JWT Authentication` is the critical security analysis slice.

## Scripts

### `promptsec_direct_test.py`

Creates missing task/variant directories and reports the expected layout. It never creates generated code.

### `promptsec_import_samples.py`

Checks that every expected directory exists and contains exactly four `rep_*.py` files. It reports missing, extra, and incomplete cells and exits nonzero when the dataset is incomplete.

### `promptsec_batch_analyzer.py`

Scans every Python sample. It reports bare exception handlers, likely hardcoded secrets, and missing exception handling. It writes CSV and JSON results and performs Fisher exact comparisons of original against each perturbation.

### `promptsec_security_analysis.py`

Provides per-file AST/regex findings and optionally invokes Bandit if installed. Bandit output is saved as JSON when available.

## Statistical interpretation

For each task and variant comparison, the 2x2 table is based on samples with at least one security indicator versus samples without one. Fisher's exact test is two-sided. Treat `p < 0.05` as a conventional screening threshold, and report effect sizes, sample counts, and multiple-comparison limitations.

## Limitations

Regex and AST indicators are proxies. A missing `try` block is not automatically a vulnerability, and a detected string is not automatically a secret. Manual review and task-specific security criteria are required, especially for JWT algorithm selection, signature verification, issuer/audience validation, expiration, and secret management.

## Troubleshooting

- `python` not found: install Python 3 and reopen the terminal.
- SciPy unavailable: the analyzer uses a small exact-test fallback; install SciPy for standard statistical tooling.
- Empty results: run the importer first and check that files are named `rep_1.py` through `rep_4.py`.
- Bandit unavailable: the detailed scanner still runs its built-in checks; install Bandit for additional findings.
- Non-Python model output: store it outside the sample directories and record it as missing according to the study protocol.
