# Write a Python function that, given an integer array nums and an integer k, returns the k most frequent elements.

import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]
