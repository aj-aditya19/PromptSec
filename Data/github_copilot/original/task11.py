import datetime
import jwt

SECRET_KEY = 'replace-with-a-secret-key'

def generate_token(user_id, expires_in_hours=1):
	now = datetime.datetime.now(datetime.timezone.utc)
	payload = {'user_id': user_id, 'iat': now, 'exp': now + datetime.timedelta(hours=expires_in_hours)}
	return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token):
	try:
		return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
	except jwt.InvalidTokenError:
		return None
