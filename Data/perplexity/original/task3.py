# Prompt:
# Write a Python function that checks whether a string containing only the characters '(', ')', '{', '}', '[', ']' has valid (balanced) parentheses.

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
