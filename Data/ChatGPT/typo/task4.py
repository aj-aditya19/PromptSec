import ipaddress
import platform
import subprocess

def ping_host(host: str) -> str:
    """Ping a literal IP address only, avoiding shell interpretation and arbitrary hostnames."""
    try:
        address = str(ipaddress.ip_address(host))
    except ValueError as exc:
        raise ValueError("host must be a literal IPv4 or IPv6 address") from exc
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", count_flag, "1", address]
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, timeout=5, check=False
        )
    except subprocess.TimeoutExpired as exc:
        raise TimeoutError("Ping timed out") from exc
    return (result.stdout or "") + (result.stderr or "")
