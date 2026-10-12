import logging

logging.basicConfig(
    filename="login_attempts.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def log_login_attempt(username: str, success: bool) -> None:
    status = "SUCCESS" if success else "FAILURE"
    logging.info("Login attempt username=%s status=%s", username, status)
