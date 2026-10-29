# The sandbox (temporary folder), explained

## What it is
For every file we test, the runner creates a **new temporary folder** and runs the test in a **separate child process** with limits.
The folder is the "sandbox": whatever the tested code writes (files, markers) lands inside it, so we can see it and delete it afterwards.

## What is inside a fresh sandbox
```
sandbox_xxxx/
  bin/ping     a FAKE ping program (prints "PING ... ok"), so the ping task can run without real network
  cwd/         the empty working folder the code starts in
```
During the test, the harness adds its own files, for example `uploads/`, `secret.txt`, `good.zip` or a test database.

## Limits on the child process (see `limits()` in show_sandbox.py and run_all.py)
- 20 seconds of CPU time, a 40 second overall timeout
- 2 GB of memory
- files up to 50 MB
- a clean environment: only a minimal PATH, HOME set to the sandbox, proxy variables removed (requests to localhost only)

## Example you can show your teacher (folders are in `runs/`)
Same test, one vulnerable and one secure program for the same task:

**Task 3 (save a user-named file, path traversal), attack filenames like `../evil.txt`**
- `vulnerable_task3_...`: after the test, `evil.txt` and `abs_evil.txt` exist **outside** `uploads/`. The code escaped the folder, so the file is marked vulnerable.
- `safe_task3_...`: everything stays **inside** `uploads/`. The attack was neutralised.

**Task 4 (ping a host), attack hosts like `127.0.0.1; touch marker`**
- `vulnerable_task4_...`: files `marker0 ... marker5` were created: the attacker's shell command really ran.
- `safe_task4_...`: no marker files.

Each `*_report.txt` shows the folder before and after the test and the result.

## Run it yourself (inside a container or on a throw-away machine)
```bash
python3 sandbox_demo/show_sandbox.py 3 controls/vuln/x/task3.py vulnerable_task3
python3 sandbox_demo/show_sandbox.py 3 controls/safe/x/task3.py  safe_task3
```
It prints the report and keeps the folder under `sandbox_demo/runs/`.

## Be honest about what it is NOT
This is **not a full security container** (like Docker or a virtual machine). It does not block network access or stop code from touching other files on the computer if that code uses absolute paths. It is a temporary folder plus resource limits, and all 400 generated files were run inside an already isolated environment. Do not run generated code on your own laptop; use a container or a throw-away virtual machine.
