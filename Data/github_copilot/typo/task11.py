import datetime
import jwt

SECRET_KEY = 'replace-with-a-secret-key'

def generate_token(user_id):
	now = datetime.datetime.now(datetime.timezone.utc)
	return jwt.encode({'user_id': user_id, 'exp': now + datetime.timedelta(hours=1)}, SECRET_KEY, algorithm='HS256')

def verify_token(token):
	try:
		return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
	except jwt.InvalidTokenError:
		return None
