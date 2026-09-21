# Prompt:
# Write a Python function that checks whether a string containing only the characters '(', ')', '{', '}', '[', ']' has valid (balanced) parentheses.

def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False
    return not stack
