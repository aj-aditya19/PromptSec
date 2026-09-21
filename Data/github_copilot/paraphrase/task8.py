from collections import Counter

def get_most_frequent(numbers, k):
	counts = Counter(numbers)
	return [number for number, _ in counts.most_common(k)]
