import ipaddress
import platform
import re
import subprocess

_HOSTNAME_RE = re.compile(
    r"^(?=.{1,253}$)([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)(\.[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*$"
)


def ping_host(host: str) -> str:
    host = host.strip()
    try:
        ipaddress.ip_address(host)
    except ValueError:
        if not _HOSTNAME_RE.match(host) or host.startswith("-"):
            raise ValueError("Invalid host")

    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", count_flag, "4", host],
        capture_output=True,
        text=True,
        timeout=30,
        shell=False,
    )
    return result.stdout + result.stderr
