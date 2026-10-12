import logging

logger = logging.getLogger(__name__)


def _sanitize(value: str, max_len: int = 100) -> str:
    # Neutralise CR/LF and other control chars to prevent log injection/forging
    value = str(value)[:max_len]
    return "".join(c if c.isprintable() else f"\\x{ord(c):02x}" for c in value)


def log_login_attempt(username: str, success: bool) -> None:
    # Never log passwords or tokens; only the (sanitised) username and outcome
    if success:
        logger.info("Login attempt: user=%r success=%s", _sanitize(username), True)
    else:
        logger.warning("Login attempt: user=%r success=%s", _sanitize(username), False)
