# Prompt:
# Implement a function in Python that looks at how often each number appears in a list and returns the k numbers that occur most often.

# Python solution below

from collections import Counter

def top_k_frequent(nums, k):
    return [value for value, _ in Counter(nums).most_common(k)]
