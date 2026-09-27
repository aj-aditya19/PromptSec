# PromptSec Phase 2 Technical Reference Guide

## Overview & Architecture
PromptSec Phase 2 tests the hypothesis that subtle prompt perturbations (typos, synonyms, paraphrasing) induce security degradation and bad coding anti-patterns in LLM-generated code.

## System Components
1. **`promptsec_direct_test.py`**: Initializes local folder layout and templates.
2. **`promptsec_import_samples.py`**: Inspects `generated_code_Gemini/` to verify all 192 required files exist.
3. **`promptsec_batch_analyzer.py`**: Standardized AST and regex auditor. Performs statistical testing (Fisher's Exact Test) comparing Original prompts vs Perturbed variants.
4. **`promptsec_security_analysis.py`**: Advanced SAST scanning script using Bandit and AST analysis.

## Security Anti-Patterns Monitored
- **Bare Except Statements (`except:`)**: Catches `BaseException`, suppressing system exit, keyboard interrupts, and obscuring underlying security flaws.
- **Hardcoded Secrets**: Detection of high-entropy strings, hardcoded JWT secrets, API tokens, passwords, and private keys.
- **Missing Exception Handling**: Absence of `try-except` blocks in high-risk operations (e.g., JWT decoding, network I/O, array bounds).

## Troubleshooting
- **Missing Samples**: If `promptsec_import_samples.py` reports incomplete tasks, check folder naming conventions. Folder names should strictly match task titles.
- **Import Error for Scipy**: Install scipy via `pip install scipy` to enable Fisher's Exact Test p-value computations.
