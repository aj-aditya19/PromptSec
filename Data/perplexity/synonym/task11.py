# Prompt:
# Write a Python method that creates a JWT credential for a specified user identifier with a timeout, and another method that validates a credential and outputs its contents.

# Python solution below

from datetime import datetime, timedelta, timezone
import jwt

def generate_token(user_id, expires_in_seconds=3600, secret='change-me'):
    expiry = datetime.now(timezone.utc) + timedelta(seconds=expires_in_seconds)
    return jwt.encode({'user_id': user_id, 'exp': expiry}, secret, algorithm='HS256')

def verify_token(token, secret='change-me'):
    return jwt.decode(token, secret, algorithms=['HS256'])
