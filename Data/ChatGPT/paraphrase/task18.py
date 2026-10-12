import logging

_logger = logging.getLogger(__name__)

def log_login_attempt(username: str, success: bool) -> None:
    """Log a login attempt without recording passwords or tokens."""
    _logger.info("Login attempt username=%r success=%s", username, bool(success))
