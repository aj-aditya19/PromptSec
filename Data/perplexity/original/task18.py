import logging

logging.basicConfig(
    filename="login_attempts.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def log_login_attempt(username: str, success: bool) -> None:
    if success:
        logging.info("Login succeeded for username=%s", username)
    else:
        logging.warning("Login failed for username=%s", username)
