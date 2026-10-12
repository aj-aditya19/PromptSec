import subprocess
import platform
import ipaddress

def ping_host(host: str) -> str:
    """Ping a validated IP address or hostname without invoking a shell."""
    candidate = host.strip()
    if not candidate or any(ch.isspace() for ch in candidate) or candidate.startswith("-"):
        raise ValueError("Invalid host")
    try:
        ipaddress.ip_address(candidate)
    except ValueError:
        import re
        if not re.fullmatch(r"(?=.{1,253}$)[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?", candidate):
            raise ValueError("Invalid host")
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", count_flag, "1", candidate],
            capture_output=True, text=True, timeout=10, check=False,
        )
        return (result.stdout + result.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return str(exc)
