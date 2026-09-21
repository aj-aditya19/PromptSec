def balanced_parentheses(parentheses: str) -> bool:
    """Use a stack to check if a string of parentheses is balanced."""
    stack = []
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    for bracket in parentheses:
        if bracket in bracket_pairs:
            stack.append(bracket)
        elif bracket in (")", "]", "}"):
            if not stack or bracket_pairs[stack.pop()] != bracket:
                return False
    return len(stack) == 0
