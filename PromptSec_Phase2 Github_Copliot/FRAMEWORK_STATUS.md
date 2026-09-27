# PromptSec Phase 2 Framework Status

## Initial status

- Model label: GitHub Copilot
- Collection progress: 0/192 samples
- Tasks: 0/12 complete
- Variants: 0/48 complete
- Analyzer: included
- Import validator: included
- Optional Bandit scanner: included
- Fisher exact testing: included

## Expected sample cell

Every task/variant directory must contain exactly:

```text
rep_1.py
rep_2.py
rep_3.py
rep_4.py
```

## Example analysis record

```json
{
  "task": "JWT Authentication",
  "variant": "original",
  "total_samples": 4,
  "bare_except": 0,
  "hardcoded": 0,
  "no_handling": 2,
  "bare_except_pct": 0.0
}
```

The example is illustrative only and is not an observed result. Run the scripts after collection to populate real results.

## Validation expectation

Before collection, the importer should report missing files. After all samples are saved, it should report 192 files and no incomplete cells. Analysis results must be retained with the raw data and model metadata.
