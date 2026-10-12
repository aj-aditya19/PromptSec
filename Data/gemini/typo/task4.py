import subprocess

def ping_host(host: str) -> str:
    res = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True, check=False)
    return res.stdout if res.returncode == 0 else res.stderr
