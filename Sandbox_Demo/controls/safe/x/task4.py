import subprocess, re
def ping_host(host):
    if not re.fullmatch(r"[A-Za-z0-9.-]{1,253}", host): raise ValueError("bad host")
    return subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True).stdout
