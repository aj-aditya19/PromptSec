def check_brackets_valid(s):
    stack = []
    matches = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in matches:
            if not stack or stack[-1] != matches[ch]:
                return False
            stack.pop()
    return len(stack) == 0
