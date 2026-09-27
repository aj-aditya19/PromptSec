# PromptSec Phase 2 Workflow

## Step 1: Generate samples

Use `TESTING_CHECKLIST.md`. Run each of the 48 variants four times. Save unmodified Python responses under the correct task and variant. Record model metadata and collection conditions.

## Step 2: Security analysis

Run `promptsec_import_samples.py`, then `promptsec_batch_analyzer.py`. Review the JWT Authentication files manually for secure verification, explicit algorithms, claims, expiry, and secret handling. Use `promptsec_security_analysis.py` and Bandit as supplementary checks.

## Step 3: Statistical testing

Use `analysis_output/fisher_tests.csv`. For each task, compare original with typo, synonym, and paraphrase using the binary outcome "at least one indicator". Report counts, percentages, p-values, and practical limitations.

## Step 4: Merge with other models

Keep model-specific raw samples and outputs separate. Normalize column names and indicator definitions before combining ChatGPT, Gemini, Copilot, Perplexity, Claude, and human baselines. Add a model column and preserve task/variant/repetition identifiers.

## Step 5: Paper update

Describe sampling, prompt variants, model settings, static-analysis rules, manual review protocol, statistical test, significance threshold, and missing-data handling. Include aggregate results and the JWT-focused analysis without claiming that screening indicators prove real-world exploitability.
