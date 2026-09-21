from collections import Counter

def top_k_frequent(nums, k):
	counts = Counter(nums)
	return [value for value, _ in counts.most_common(k)]
