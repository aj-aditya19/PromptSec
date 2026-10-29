"""Show what the test sandbox is: a temporary folder + a child process with limits.
Runs ONE generated file against ONE task test and KEEPS the temporary folder so you can look inside.

Usage (from the project root, where harness.py is):
    python3 sandbox_demo/show_sandbox.py <task_number> <path_to_file.py> <label>
Example:
    python3 sandbox_demo/show_sandbox.py 3 controls/vuln/x/task3.py vulnerable_task3
"""
import os, sys, re, json, subprocess, tempfile, resource

def limits():                                   # limits applied to the child process
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))                      # 20 s of CPU
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))     # 2 GB memory
    resource.setrlimit(resource.RLIMIT_FSIZE, (50 * 1024**2, 50 * 1024**2))# files up to 50 MB

def tree(root):
    lines = []
    for d, dirs, files in os.walk(root):
        dirs.sort(); rel = os.path.relpath(d, root)
        depth = 0 if rel == "." else rel.count(os.sep) + 1
        if rel != ".": lines.append("  " * depth + os.path.basename(d) + "/")
        for f in sorted(files):
            lines.append("  " * (depth + 1) + f)
    return "\n".join(lines)

task, path, label = int(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs"); os.makedirs(base, exist_ok=True)
tmp = tempfile.mkdtemp(prefix=label + "_", dir=base)           # 1) the temporary folder (the sandbox)
os.makedirs(f"{tmp}/bin"); os.makedirs(f"{tmp}/cwd")
open(f"{tmp}/bin/ping", "w").write('#!/bin/sh\necho "PING $* ok"\n'); os.chmod(f"{tmp}/bin/ping", 0o755)   # fake ping
before = tree(tmp)
env = {"PATH": f"{tmp}/bin:/usr/local/bin:/usr/bin:/bin", "HOME": tmp, "PS_TMP": tmp, "LANG": "C.UTF-8",
       "NO_PROXY": "127.0.0.1,localhost", "PYTHONDONTWRITEBYTECODE": "1"}
harness = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "harness.py")
p = subprocess.run([sys.executable, harness, str(task), path], cwd=f"{tmp}/cwd", env=env, capture_output=True,
                   text=True, timeout=40, preexec_fn=limits, input="")      # 2) child process with limits and a timeout
res = json.loads(re.findall(r"@@RESULT@@(\{.*\})", p.stdout)[-1])
report = f"""SANDBOX REPORT: {label}
Tested file : {sys.argv[2]}   (task {task})
Sandbox     : {os.path.relpath(tmp)}

--- Folder BEFORE the test (created empty, only the fake ping and an empty working folder) ---
{before}

--- Folder AFTER the test (files created by the test and by the tested code) ---
{tree(tmp)}

--- Result ---
functional test passed : {res['func']}
security flags (True = weakness found): {json.dumps(res['flags'])}
"""
open(os.path.join(base, label + "_report.txt"), "w").write(report)
print(report)
