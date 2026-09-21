import datetime
import jwt

SECRET = 'replace-with-a-secret-key'

def create_credential(user_identifier):
	expiry = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
	return jwt.encode({'user_id': user_identifier, 'exp': expiry}, SECRET, algorithm='HS256')

def validate_credential(credential):
	try:
		return jwt.decode(credential, SECRET, algorithms=['HS256'])
	except jwt.InvalidTokenError:
		return None
