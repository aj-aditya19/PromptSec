import platform
import subprocess


def ping_host(host: str) -> str:
    if not host or any(character in host for character in "\r\n;&|`$<>"):
        raise ValueError("Invalid host")
    command = (
        ["ping", "-n", "1", host]
        if platform.system() == "Windows"
        else ["ping", "-c", "1", host]
    )
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    return (result.stdout + result.stderr).strip()
