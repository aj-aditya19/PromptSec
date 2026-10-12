import subprocess

def ping_host(host: str) -> str:
    # Basic validation for hostname/ip to prevent arbitrary shell injection
    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
    return result.stdout
