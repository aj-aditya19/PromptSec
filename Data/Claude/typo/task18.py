import logging

logger = logging.getLogger(__name__)


def _sanitize(value: str, max_len: int = 100) -> str:
    # Prevent log injection: escape CR/LF and other control characters.
    cleaned = "".join(
        c if c.isprintable() else f"\\x{ord(c):02x}" for c in str(value)
    )
    return cleaned[:max_len]


def log_login_attempt(username: str, success: bool) -> None:
    # Never log passwords or tokens.
    logger.info(
        "login_attempt username=%r success=%s",
        _sanitize(username),
        bool(success),
    )
