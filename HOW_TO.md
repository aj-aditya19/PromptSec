# HOW TO (batch method): 4 chats per model

Per model you do only **4 chats** (one per variant). Each chat has all 20 tasks.
Total: 5 models x 4 variants = **20 chats** -> 400 files.

## Files you have
- `batch_original.txt`, `batch_typo.txt`, `batch_synonym.txt`, `batch_paraphrase.txt` : paste one whole file into one chat
- `split_responses.py` : splits the saved answers into task files automatically

## Steps (for each model, for each variant)

1. Open a **new chat** in the tool.
2. Copy the **whole** `batch_<variant>.txt` and paste it. Send. Nothing else.
3. Copy the **whole answer** of the model (text and code blocks, all of it).
4. Save it in a text file here:

```
responses/<model>/<variant>.txt
```

Example: `responses/claude/typo.txt`

Model folder names: `claude`, `chatgpt`, `gemini`, `copilot`, `perplexity`
Variant names: `original`, `typo`, `synonym`, `paraphrase`

5. Add one line to `metadata.csv` (one line per chat):

```
model,model_version,date,interface,variant,response_file,notes
claude,<version shown in app>,2026-10-12,web,typo,responses/claude/typo.txt,
```

## If the answer is cut in the middle
Type only: `continue from task N` (N = the next task). Copy that part too and paste it **at the end of the same .txt file**. Write "continued" in `notes` in metadata.csv.

## Split into task files (do this when you have some or all responses)

```bash
python split_responses.py
```

It creates:

```
ai_code/claude/original/task1.py ... task20.py
ai_code/claude/typo/task1.py ... task20.py
...
```

and prints which tasks are missing. If a task is missing, ask the model again in a new chat for that variant (all 20 again), do not patch by hand, and note it in `notes`.

## Human code
Unchanged: 20 files in `human_code/task1.py ... task20.py`, written by you from OWASP or the official Python docs. Same function names as in the prompts. Put the sources in `human_code/SOURCES.md`.

## Do not run the generated code on your computer
Ping, zip and file-save tasks can be dangerous with bad input. I will test in a sandbox.

## Send me
Zip the folder with `responses/`, `ai_code/`, `human_code/` and `metadata.csv`.

## Note for the paper (important)
All 20 tasks are in one chat, so earlier tasks can influence later ones. Say this in Limitations. Keep the task order the same in every chat (the files already do this).
