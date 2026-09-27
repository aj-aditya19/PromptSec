from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    Write a Python function that, given an integer array nums and an integer k, 
    returns the k most frequent elements.
    """
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
