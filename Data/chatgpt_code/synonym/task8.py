# Prompt:
# Write a Python method that, given a list of integers and an integer k, returns the k most common values.

from collections import Counter

def top_k_frequent(nums, k):
    return [num for num, _ in Counter(nums).most_common(k)]
