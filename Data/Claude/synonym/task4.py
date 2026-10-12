import ipaddress
import platform
import re
import subprocess

_HOSTNAME_RE = re.compile(
    r"^(?=.{1,253}$)([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)(\.[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*$"
)


def _validate_host(host: str) -> str:
    if not isinstance(host, str):
        raise ValueError("Invalid host")
    host = host.strip()
    try:
        ipaddress.ip_address(host)
        return host
    except ValueError:
        pass
    if host.startswith("-") or not _HOSTNAME_RE.match(host):
        raise ValueError("Invalid host")
    return host


def ping_host(host: str) -> str:
    host = _validate_host(host)
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = ["ping", count_flag, "4", host]
    result = subprocess.run(
        cmd, capture_output=True, text=True, timeout=30, shell=False
    )
    return result.stdout + result.stderr
