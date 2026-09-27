def length_of_longest_substring(s):
    """
    Write a Python function that finds the length of the longest substring 
    without repeating characters in a given string.
    """
    char_index_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
