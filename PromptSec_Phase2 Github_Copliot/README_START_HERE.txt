PromptSec Phase 2 Framework - GitHub Copilot
============================================

Purpose
-------
This folder contains the complete Phase 2 experiment framework for studying whether prompt perturbations affect the security of AI-generated Python code.

Experiment design
-----------------
12 coding tasks x 4 prompt variants x 4 repetitions = 192 samples.
Variants: original, typo, synonym, paraphrase.
JWT Authentication is the primary security-critical task.

Start here
----------
1. Read QUICKSTART.md.
2. Use TESTING_CHECKLIST.md while collecting one response per prompt and repetition.
3. Save each response as rep_1.py through rep_4.py in the matching task/variant directory.
4. Run promptsec_import_samples.py to validate completeness.
5. Run promptsec_batch_analyzer.py for metrics, CSV, JSON, and Fisher exact tests.
6. Optionally run promptsec_security_analysis.py for Bandit and detailed findings.

Files
-----
- QUICKSTART.md: practical collection and analysis steps.
- TESTING_CHECKLIST.md: all 48 prompts, ready to copy and paste.
- README_PHASE2.md: full reference and troubleshooting.
- PHASE2_WORKFLOW.md: five-stage research workflow.
- FRAMEWORK_STATUS.md: initial progress and validation status.
- COMPLETE_FRAMEWORK_SUMMARY.txt: deliverables and success criteria.
- promptsec_direct_test.py: creates or verifies the sample template.
- promptsec_import_samples.py: validates sample counts.
- promptsec_batch_analyzer.py: produces aggregate security analysis.
- promptsec_security_analysis.py: detailed regex, AST, and optional Bandit scan.

Generated outputs
-----------------
Analysis output is written to analysis_output/ inside this folder. Existing project files are not required or modified.
