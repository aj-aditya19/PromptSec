import logging

def log_login_attempt(username: str, success: bool) -> None:
    logger = logging.getLogger("auth")
    status = "SUCCESS" if success else "FAILED"
    logger.info(f"Login attempt for user '{username}': {status}")
