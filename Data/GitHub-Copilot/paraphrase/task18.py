import logging


def log_login_attempt(username: str, success: bool) -> None:
    logging.getLogger(__name__).info(
        "Login attempt username=%r success=%s",
        username,
        success,
    )
