# Prompt:
# Write a Python fucntion that, given an integr aray nums and an integer k, returns the k most frequnt elemnts.

# Python solution below

from collections import Counter

def top_k_frequent(nums, k):
    return [value for value, _ in Counter(nums).most_common(k)]
