from collections import Counter
import heapq

def top_k_common(nums, k):
    """
    Write a Python method that, given a list of integers and an integer k, 
    returns the k most common values.
    """
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
