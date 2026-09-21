def length_of_longest_substring(s):
    char_index = {}
    max_len = 0
    start = 0
    for i, c in enumerate(s):
        if c in char_index and char_index[c] >= start:
            start = char_index[c] + 1
        char_index[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len
