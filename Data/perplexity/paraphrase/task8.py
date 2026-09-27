from collections import Counter
import heapq

def get_k_most_frequent_numbers(nums, k):
    """
    Implement a function in Python that looks at how often each number appears 
    in a list and returns the k numbers that occur most often.
    """
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
