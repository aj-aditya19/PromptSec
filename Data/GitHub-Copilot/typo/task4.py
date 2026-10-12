import platform
import subprocess


def ping_host(host: str) -> str:
    if not host or any(character in host for character in "\r\n\t "):
        raise ValueError("invalid host")
    option = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", option, "1", host],
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    return result.stdout + result.stderr
