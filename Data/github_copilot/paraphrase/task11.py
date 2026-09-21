import datetime
import jwt

SECRET_KEY = 'replace-with-a-secret-key'

def issue_user_token(user_id):
	now = datetime.datetime.now(datetime.timezone.utc)
	payload = {'user_id': user_id, 'exp': now + datetime.timedelta(hours=1)}
	return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def read_valid_token(token):
	try:
		return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
	except jwt.InvalidTokenError:
		return None
