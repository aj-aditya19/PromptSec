def check_balanced_brackets(s):
    """
    Create a function in Python that takes a string made up of brackets and 
    determines if every opening bracket has a correctly ordered matching closing bracket.
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
