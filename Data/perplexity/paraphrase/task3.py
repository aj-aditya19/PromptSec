# Prompt:
# Create a function in Python that takes a string made up of brackets and determines if every opening bracket has a correctly ordered matching closing bracket.

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
