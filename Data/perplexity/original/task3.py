def is_valid_parentheses(s):
    """
    Write a Python function that checks whether a string containing only the characters 
    '(', ')', '{', '}', '[', ']' has valid (balanced) parentheses.
    """
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
