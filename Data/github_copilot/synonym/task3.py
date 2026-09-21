def has_matched_brackets(text):
	stack = []
	pairs = {')': '(', ']': '[', '}': '{'}
	for symbol in text:
		if symbol in '([{':
			stack.append(symbol)
		elif symbol in pairs:
			if not stack or stack.pop() != pairs[symbol]:
				return False
	return not stack
