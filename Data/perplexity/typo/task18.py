import logging

logger = logging.getLogger(__name__)

def log_login_attempt(username: str, success: bool) -> None:
    logging.basicConfig(level=logging.INFO)
    safe_username = username.replace("\r", "").replace("\n", "")
    if success:
        logger.info("Login succeeded for username=%s", safe_username)
    else:
        logger.warning("Login failed for username=%s", safe_username)
