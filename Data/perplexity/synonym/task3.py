# Prompt:
# Write a Python method that verifies whether a string consisting only of the symbols '(', ')', '{', '}', '[', ']' has proper (matched) brackets.

# Python solution below

def is_valid_parentheses(s):
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    return not stack
