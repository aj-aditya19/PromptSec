def is_valid(s):
	stack = []
	pairs = {')': '(', ']': '[', '}': '{'}
	for char in s:
		if char in '([{':
			stack.append(char)
		elif char in pairs:
			if not stack or stack.pop() != pairs[char]:
				return False
	return not stack
