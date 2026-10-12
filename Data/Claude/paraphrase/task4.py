import platform
import re
import subprocess

_HOST_RE = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9.\-]{0,251}[A-Za-z0-9])?$|^[0-9a-fA-F:]+$")


def ping_host(host: str) -> str:
    if not isinstance(host, str) or not _HOST_RE.match(host) or host.startswith("-"):
        raise ValueError("Invalid hostname")
    count_flag = "-n" if platform.system() == "Windows" else "-c"
    result = subprocess.run(
        ["ping", count_flag, "4", host],
        capture_output=True,
        text=True,
        timeout=30,
        shell=False,
    )
    return result.stdout + result.stderr
