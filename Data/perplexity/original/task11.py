# Prompt:
# Write a Python function that generates a JWT token for a given user ID with an expiration time, and another function that verifies a token and returns its payload.

# Python solution below

from datetime import datetime, timedelta, timezone
import jwt

def generate_token(user_id, expires_in_seconds=3600, secret='change-me'):
    expiry = datetime.now(timezone.utc) + timedelta(seconds=expires_in_seconds)
    return jwt.encode({'user_id': user_id, 'exp': expiry}, secret, algorithm='HS256')

def verify_token(token, secret='change-me'):
    return jwt.decode(token, secret, algorithms=['HS256'])
