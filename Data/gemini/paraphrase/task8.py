# Implement a function in Python that looks at how often each number appears in a list and returns the k numbers that occur most often.

import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]
