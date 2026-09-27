def max_unique_consecutive_length(s):
    """
    Implement a function in Python that scans a string and returns how long 
    the longest stretch of consecutive characters is, where no character 
    appears more than once in that stretch.
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
