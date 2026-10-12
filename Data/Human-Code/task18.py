import logging

def log_login_attempt(username: str, success: bool) -> None:
    
    logging.basicConfig(level=logging.INFO)

    if success:
        logging.info("Login successful for user: %s", username)
    else:
        logging.warning("Login failed for user: %s", username)
