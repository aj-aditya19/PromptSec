# Write a Python fucntion that cheks wether a string containg only the characters '(', ')', '{', '}', '[', ']' has valid (balancd) parenthesis.

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
