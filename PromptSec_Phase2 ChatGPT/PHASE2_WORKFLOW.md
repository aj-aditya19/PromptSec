# PromptSec Phase 2 Workflow

## Step 1 — Generate samples

For each of the 12 tasks:
1. Open TESTING_CHECKLIST.md.
2. Submit the Original prompt four times.
3. Submit the Typo prompt four times.
4. Submit the Synonym prompt four times.
5. Submit the Paraphrase prompt four times.
6. Save every generated Python solution in the matching directory.

Result: 16 samples per task and 192 samples for the model.

Maintain the same model, model version/configuration, temperature/settings,
and system/developer instructions across the experiment where the research
protocol requires comparability. Record configuration metadata separately.

## Step 2 — Security analysis

Run:
```bash
python promptsec_batch_analyzer.py
```

Review:
- bare except
- hardcoded-secret heuristic
- no exception handling
- task/variant percentages
- per-sample findings
- JWT Authentication results

Optionally run:
```bash
python promptsec_security_analysis.py
```

Use qualitative review for security properties that regex/Bandit cannot
reliably establish, especially JWT verification behavior.

## Step 3 — Statistical testing

The main analyzer creates 2×2 tables and performs Fisher's exact tests for
Original vs each perturbation.

Interpret:
- p < 0.05: statistically significant under the chosen threshold;
- p ≥ 0.05: not statistically significant under that threshold.

Do not interpret a p-value as the probability that the hypothesis is true.
Also consider effect sizes, sample counts, multiple comparisons, and the
limitations of the indicators.

## Step 4 — Merge with other models

Repeat the same protocol for:
- Claude
- ChatGPT
- Gemini
- Copilot
- Perplexity

Keep model directories separate.

When comparing models, preserve:
- task identity;
- variant identity;
- repetition count;
- model/version metadata;
- collection dates/settings.

Do not silently merge incomplete datasets.

## Step 5 — Paper update

Report:
- experimental design;
- prompt variants;
- number of repetitions;
- security indicators;
- analysis method;
- Fisher's exact test setup;
- task-level results;
- JWT-focused qualitative findings;
- limitations.

Avoid claiming that prompt perturbation causes security changes solely from
observational output differences. Discuss statistical evidence together with
qualitative security review and experimental controls.
