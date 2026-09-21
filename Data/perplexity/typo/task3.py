# Prompt:
# Write a Python fucntion that cheks wether a string containg only the characters '(', ')', '{', '}', '[', ']' has valid (balancd) parenthesis.

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
