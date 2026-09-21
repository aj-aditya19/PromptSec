# Prompt:
# Write a Python fucntion that cheks wether a string containg only the characters '(', ')', '{', '}', '[', ']' has valid (balancd) parenthesis.

def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False
    return not stack
