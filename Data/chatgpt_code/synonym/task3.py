# Prompt:
# Write a Python method that verifies whether a string consisting only of the symbols '(', ')', '{', '}', '[', ']' has proper (matched) brackets.

def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False
    return not stack
