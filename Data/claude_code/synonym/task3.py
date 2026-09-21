def has_matched_brackets(text):
    bracket_stack = []
    closing_to_opening = {')': '(', '}': '{', ']': '['}
    for character in text:
        if character in closing_to_opening:
            if not bracket_stack or bracket_stack.pop() != closing_to_opening[character]:
                return False
        elif character in '({[':
            bracket_stack.append(character)
    return not bracket_stack
