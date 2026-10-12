import logging


logger = logging.getLogger(__name__)


def log_login_attempt(username: str, success: bool) -> None:
    logger.info("Login attempt for username=%r success=%s", username, success)
