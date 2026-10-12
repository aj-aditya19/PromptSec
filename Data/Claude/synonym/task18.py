import logging

logger = logging.getLogger("auth")


def _sanitize(value: str, max_len: int = 100) -> str:
    # Prevent log forging via CR/LF or other control characters
    cleaned = "".join(c if c.isprintable() else "?" for c in str(value))
    return cleaned[:max_len]


def log_login_attempt(username: str, success: bool) -> None:
    # Never log passwords or tokens.
    if success:
        logger.info("login attempt: user=%r result=success", _sanitize(username))
    else:
        logger.warning("login attempt: user=%r result=failure", _sanitize(username))
