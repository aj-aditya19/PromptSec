from collections import Counter

def get_k_most_frequent(nums, k):
    freq_map = Counter(nums)
    sorted_by_freq = sorted(freq_map, key=freq_map.get, reverse=True)
    return sorted_by_freq[:k]
