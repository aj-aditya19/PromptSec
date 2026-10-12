import logging

logger = logging.getLogger("auth_logger")
logging.basicConfig(level=logging.INFO)

def log_login_attempt(username: str, success: bool) -> None:
    sanitized_user = username.replace("
", "").replace("", "")
    status = "SUCCESS" if success else "FAILED"
    logger.info("Login attempt for user '%s': %s", sanitized_user, status)
