from collections import Counter

def top_k_frequent(nums, k):
	return [item for item, _ in Counter(nums).most_common(k)]
