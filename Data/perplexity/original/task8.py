# Prompt:
# Write a Python function that, given an integer array nums and an integer k, returns the k most frequent elements.

# Python solution below

from collections import Counter

def top_k_frequent(nums, k):
    return [value for value, _ in Counter(nums).most_common(k)]
