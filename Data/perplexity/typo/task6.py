# Prompt:
# Write a Python fucntion that finds the lenght of the longst substring withuot repeating charecters in a given string.

# Python solution below

def longest_substring_without_repeating(s):
    last_seen, left, longest = {}, 0, 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        longest = max(longest, right - left + 1)
    return longest
