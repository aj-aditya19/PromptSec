from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    Given an integer array nums and an integer k, return the k most
    frequent elements.
    """
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
