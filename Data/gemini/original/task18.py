import logging

logging.basicConfig(level=logging.INFO)

def log_login_attempt(username: str, success: bool) -> None:
    status = "SUCCESS" if success else "FAILED"
    logging.info(f"Login attempt for user '{username}': {status}")
