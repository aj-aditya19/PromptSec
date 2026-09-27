# PromptSec Phase 2 End-to-End Workflow

```
[ Step 1: Prompt Execution ] ──> [ Step 2: Import Validation ]
                                            │
[ Step 4: Cross-Model Merge ] <── [ Step 3: Security & Stat Analysis ]
            │
            ▼
[ Step 5: Research Paper Update ]
```

---

### Step 1: Generate & Collect Samples
- Execute each of the 4 prompt variants across 12 tasks on **Gemini**.
- Repeat each variant 4 times in independent sessions.
- Store output in `generated_code_Gemini/<Task_Name>/<variant>/rep_<1-4>.py`.

---

### Step 2: Security Pattern Analysis
- Run `promptsec_batch_analyzer.py` to check for:
  - `bare_except`
  - `hardcoded_secrets`
  - `no_exception_handling`

---

### Step 3: Statistical Hypothesis Testing
- For each perturbed variant (Typo, Synonym, Paraphrase), a 2x2 contingency matrix is constructed against the Original variant:
  
  | Group | Defective (Vulnerable) | Non-Defective (Secure) |
  |---|---|---|
  | Original | a | b |
  | Perturbation | c | d |

- Compute Fisher's Exact Test p-value. p < 0.05 indicates a statistically significant impact caused by prompt perturbation.

---

### Step 4: Cross-Model Merging
- Merge `promptsec_results_Gemini.json` into the master repository alongside results from ChatGPT, Claude, Copilot, and Perplexity.

---

### Step 5: Paper Synthesis
- Compile comparative vulnerability matrices and publish p-value heatmaps in the research paper.
