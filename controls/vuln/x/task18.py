import logging
logging.basicConfig(level=logging.INFO)
def log_login_attempt(username, success):
    logging.info(f"Login attempt for user {username}: {'ok' if success else 'failed'}")
