# Write a Python method that, given a list of integers and an integer k, returns the k most common values.

import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]
