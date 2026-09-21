def length_of_longest_substring(s):
    seen = {}
    result = 0
    left = 0
    for right in range(len(s)):
        c = s[right]
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = right
        result = max(result, right - left + 1)
    return result
