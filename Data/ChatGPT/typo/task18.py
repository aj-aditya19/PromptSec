import logging

logger = logging.getLogger(__name__)

def log_login_attempt(username: str, success: bool) -> None:
    """Log login outcome without including passwords or other credentials."""
    logger.info("Login attempt username=%r success=%s", username, bool(success))
