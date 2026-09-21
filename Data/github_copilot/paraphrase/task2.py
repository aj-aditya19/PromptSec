def find_pair_indices(numbers, target):
	seen = {}
	for index, number in enumerate(numbers):
		remainder = target - number
		if remainder in seen:
			return [seen[remainder], index]
		seen[number] = index
	return []
