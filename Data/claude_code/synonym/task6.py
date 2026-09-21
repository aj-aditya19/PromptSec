def longest_unique_substring_length(text):
    last_seen = {}
    best = 0
    window_start = 0
    for index, letter in enumerate(text):
        if letter in last_seen and last_seen[letter] >= window_start:
            window_start = last_seen[letter] + 1
        last_seen[letter] = index
        best = max(best, index - window_start + 1)
    return best
