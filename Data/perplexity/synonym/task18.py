import logging

def log_login_attempt(username: str, success: bool) -> None:
    logging.basicConfig(level=logging.INFO)
    status = "succeeded" if success else "failed"
    logging.info("Login attempt for user %s %s", username, status)
