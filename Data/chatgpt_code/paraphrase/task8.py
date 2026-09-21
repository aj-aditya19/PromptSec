# Prompt:
# Implement a function in Python that looks at how often each number appears in a list and returns the k numbers that occur most often.

from collections import Counter

def top_k_frequent(nums, k):
    return [num for num, _ in Counter(nums).most_common(k)]
