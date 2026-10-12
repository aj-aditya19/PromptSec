import logging

_logger = logging.getLogger(__name__)

def log_login_attempt(username: str, success: bool) -> None:
    """Record a login attempt without logging credentials."""
    _logger.info("Login attempt username=%r success=%s", username, bool(success))
