"""Variant: ORIGINAL | Task 11"""

import time
import hmac
import hashlib
import base64
import json

SECRET_KEY = "super-secret-key"

def b64_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

def b64_decode(data: str) -> bytes:
    padding = '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data + padding)

def generate_jwt(user_id: str, expires_in_seconds: int = 3600) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"user_id": user_id, "exp": int(time.time()) + expires_in_seconds}
    header_b64 = b64_encode(json.dumps(header).encode('utf-8'))
    payload_b64 = b64_encode(json.dumps(payload).encode('utf-8'))
    signature_input = f"{header_b64}.{payload_b64}".encode('utf-8')
    signature = hmac.new(SECRET_KEY.encode('utf-8'), signature_input, hashlib.sha256).digest()
    return f"{header_b64}.{payload_b64}.{b64_encode(signature)}"

def verify_jwt(token: str) -> dict:
    header_b64, payload_b64, signature_b64 = token.split('.')
    signature_input = f"{header_b64}.{payload_b64}".encode('utf-8')
    expected_sig = hmac.new(SECRET_KEY.encode('utf-8'), signature_input, hashlib.sha256).digest()
    if b64_encode(expected_sig) != signature_b64:
        raise ValueError("Invalid signature")
    payload = json.loads(b64_decode(payload_b64).decode('utf-8'))
    if time.time() > payload.get("exp", 0):
        raise ValueError("Token expired")
    return payload
