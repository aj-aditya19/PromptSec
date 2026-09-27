================================================================================
PROMPTSEC PHASE 2 TESTING FRAMEWORK (GEMINI)
================================================================================

Welcome to the PromptSec Phase 2 Framework for evaluating Gemini!

OVERVIEW:
This framework is designed to evaluate how prompt perturbations (Original, 
Typo, Synonym, Paraphrase) affect the security and code quality of AI-generated 
code across 12 standard algorithmic and system tasks, with a primary focus on 
Task 11: JWT Authentication.

TOTAL SAMPLING REQUIREMENT:
- 12 Tasks
- 4 Prompt Variants per task
- 4 Repetitions (n=4) per variant
- Total Code Samples: 12 x 4 x 4 = 192 Python files

DIRECTORY STRUCTURE:
- /generated_code_Gemini/ : Storage directory for all 192 samples.
- Script files: python utilities for framework setup, sample import, security auditing, and statistical testing.
- Documentation files: detailed guides, checklists, workflow steps, and status trackers.

QUICK START STEPS:
1. Review QUICKSTART.md for step-by-step instructions.
2. Refer to TESTING_CHECKLIST.md to copy-paste prompts into Gemini.
3. Save generated code into /generated_code_Gemini/<Task_Name>/<variant>/rep_<1-4>.py
4. Run `python3 promptsec_import_samples.py` to verify structure and completeness.
5. Run `python3 promptsec_batch_analyzer.py` to run security checks & Fisher's exact test.

STATUS:
Current progress: 0/192 samples collected for Gemini.
Target Security Focus: JWT Authentication (Task 11).
================================================================================
