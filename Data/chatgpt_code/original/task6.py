# Prompt:
# Write a Python function that finds the length of the longest substring without repeating characters in a given string.

def length_of_longest_substring(s):
    last_seen = {}
    left = 0
    longest = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        longest = max(longest, right - left + 1)
    return longest
