from collections import Counter
import heapq

def top_k_frequent(nums, k):
    counts = Counter(nums)
    result = heapq.nlargest(k, counts.keys(), key=lambda x: counts[x])
    return result
