PromptSec Phase 2 Framework — ChatGPT
=========================================

PURPOSE
-------
This framework supports Phase 2 of the PromptSec research project:
"Does prompt perturbation affect the security of AI-generated code?"

Experimental design:
- 12 coding tasks
- 4 prompt variants per task: Original, Typo, Synonym, Paraphrase
- 4 independent repetitions per variant
- 16 samples per task
- 192 total generated-code samples per model

START HERE
----------
1. Read QUICKSTART.md.
2. Review TESTING_CHECKLIST.md.
3. Generate/save samples under generated_code_ChatGPT/.
4. Run promptsec_import_samples.py to validate completeness.
5. Run promptsec_batch_analyzer.py to calculate security metrics and Fisher's exact tests.
6. Optionally run promptsec_security_analysis.py for Bandit-based analysis.
7. Use PHASE2_WORKFLOW.md for the full research workflow.

FILES
-----
README_START_HERE.txt        Entry point.
QUICKSTART.md                Step-by-step operating guide.
TESTING_CHECKLIST.md         All 48 prompt variants, copy-paste ready; repeat each 4 times.
README_PHASE2.md             Complete framework reference and troubleshooting.
PHASE2_WORKFLOW.md           Five-step research workflow.
FRAMEWORK_STATUS.md          Initial progress/status template.
COMPLETE_FRAMEWORK_SUMMARY.txt Full package summary.
promptsec_batch_analyzer.py  Main security/statistical analysis.
promptsec_import_samples.py  Sample-directory validator.
promptsec_security_analysis.py Optional Bandit/deep security scanner.
promptsec_direct_test.py     Framework setup utility.
generated_code_ChatGPT/      Destination for the 192 model outputs.

IMPORTANT EXPERIMENTAL RULE
---------------------------
For each prompt variant, perform four separate generations. Save only the model's
code in the corresponding rep_1.py ... rep_4.py file. Keep the prompt wording
fixed within a variant. Do not silently repair typos or alter prompts.

SECURITY SCOPE
--------------
The supplied protocol checks:
- bare except
- hardcoded-secret patterns
- absence of exception handling

These are heuristic indicators, not a complete security assessment. The JWT
Authentication task is the main security-focused task. Use the optional Bandit
scan for deeper analysis.

EXPECTED COMPLETION
-------------------
192/192 code samples present, validated, analyzed, and included in the research
dataset for this model.
