import logging


logger = logging.getLogger(__name__)


def log_login_attempt(username: str, success: bool) -> None:
    logger.info("login attempt username=%s success=%s", username, success)
