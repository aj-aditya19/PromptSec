def is_valid_parentheses(text):
	stack = []
	closing = {')': '(', ']': '[', '}': '{'}
	for character in text:
		if character in '([{':
			stack.append(character)
		elif character in closing:
			if not stack or stack.pop() != closing[character]:
				return False
	return not stack
