# Prompt:
# Write a Python function that, given an integer array nums and an integer k, returns the k most frequent elements.

from collections import Counter

def top_k_frequent(nums, k):
    return [num for num, _ in Counter(nums).most_common(k)]
