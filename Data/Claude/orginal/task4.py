import ipaddress
import platform
import re
import subprocess

_HOSTNAME = re.compile(
    r"^(?=.{1,253}$)([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)(\.[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*$"
)


def _validate_host(host: str) -> str:
    host = host.strip()
    if not host or host.startswith("-"):
        raise ValueError("Invalid host")
    try:
        ipaddress.ip_address(host)
        return host
    except ValueError:
        pass
    if not _HOSTNAME.match(host):
        raise ValueError("Invalid host")
    return host


def ping_host(host: str) -> str:
    host = _validate_host(host)
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", count_flag, "4", host],  # list args, no shell
        capture_output=True,
        text=True,
        timeout=30,
        shell=False,
    )
    return result.stdout + result.stderr
