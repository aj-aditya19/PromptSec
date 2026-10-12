import logging
logging.basicConfig(level=logging.INFO)
def log_login_attempt(username, success):
    logging.info("Login attempt for user %r: %s", username, "ok" if success else "failed")
