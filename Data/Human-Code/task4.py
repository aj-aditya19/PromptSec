import subprocess

def ping_host(host: str) -> str:
    result = subprocess.run(
        ["ping", "-c", "4", host],
        capture_output=True,
        text=True
    )

    return result.stdout
