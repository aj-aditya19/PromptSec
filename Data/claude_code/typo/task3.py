def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top != pairs[char]:
                return False
        else:
            stack.append(char)
    return len(stack) == 0
