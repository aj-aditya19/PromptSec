import subprocess
import platform
import ipaddress
import socket

def ping_host(host: str) -> str:
    """Ping a literal IP address or a hostname that resolves to an IP address."""
    candidate = host.strip()
    if not candidate or any(c.isspace() for c in candidate) or candidate.startswith("-"):
        raise ValueError("Invalid host")
    try:
        ipaddress.ip_address(candidate)
    except ValueError:
        try:
            socket.getaddrinfo(candidate, None)
        except socket.gaierror as exc:
            raise ValueError("Host could not be resolved") from exc
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", count_flag, "1", candidate],
        capture_output=True, text=True, timeout=10, check=False,
    )
    return (result.stdout + result.stderr)
