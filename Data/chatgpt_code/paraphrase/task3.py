# Prompt:
# Create a function in Python that takes a string made up of brackets and determines if every opening bracket has a correctly ordered matching closing bracket.

def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False
    return not stack
