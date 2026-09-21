from collections import Counter

def most_common_values(numbers, k):
	return [value for value, _ in Counter(numbers).most_common(k)]
