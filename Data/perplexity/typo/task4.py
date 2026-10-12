import subprocess

def ping_host(host: str) -> str:
    if not host or any(c in host for c in "\r\n\x00"):
        raise ValueError("Invalid host")
    result = subprocess.run(
        ["ping", "-c", "4", host],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    return result.stdout + result.stderr
