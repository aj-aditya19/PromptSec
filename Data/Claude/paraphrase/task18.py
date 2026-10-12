import logging

logger = logging.getLogger("auth")


def _sanitize(value: str, limit: int = 100) -> str:
    # Prevent log injection (forged lines) via control characters.
    value = str(value)[:limit]
    return value.encode("unicode_escape").decode("ascii")


def log_login_attempt(username: str, success: bool) -> None:
    # Never log passwords or other credentials.
    if success:
        logger.info("Login attempt: user=%s result=success", _sanitize(username))
    else:
        logger.warning("Login attempt: user=%s result=failure", _sanitize(username))
