import platform
import subprocess

def ping_host(host: str) -> str:
    """Ping a host without invoking a shell."""
    if not host or any(c.isspace() for c in host) or host.startswith("-"):
        raise ValueError("Invalid host")
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", count_flag, "1", host],
            capture_output=True, text=True, timeout=10, check=False,
        )
    except subprocess.TimeoutExpired:
        return "Ping timed out"
    return (result.stdout + result.stderr).strip()
