def verify_brackets(s):
    """
    Write a Python method that verifies whether a string consisting only of the symbols 
    '(', ')', '{', '}', '[', ']' has proper (matched) brackets.
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
