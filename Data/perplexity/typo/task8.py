from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    Write a Python fucntion that, given an integr aray nums and an integer k, 
    returns the k most frequnt elemnts.
    """
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
