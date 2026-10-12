import platform
import subprocess


def ping_host(host: str) -> str:
    if not host or any(character in host for character in "\r\n"):
        raise ValueError("invalid host")
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", count_flag, "4", host],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )
    return result.stdout + result.stderr
