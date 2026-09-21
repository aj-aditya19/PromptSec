def find_longest_no_repeat(s):
    positions = {}
    longest = 0
    left_ptr = 0
    for right_ptr in range(len(s)):
        ch = s[right_ptr]
        if ch in positions and positions[ch] >= left_ptr:
            left_ptr = positions[ch] + 1
        positions[ch] = right_ptr
        longest = max(longest, right_ptr - left_ptr + 1)
    return longest
