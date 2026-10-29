import subprocess
def ping_host(host):
    return subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True).stdout
