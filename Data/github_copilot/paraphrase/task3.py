def check_brackets(text):
	stack = []
	matching = {')': '(', ']': '[', '}': '{'}
	for character in text:
		if character in '([{':
			stack.append(character)
		elif character in matching:
			if not stack or stack.pop() != matching[character]:
				return False
	return not stack
