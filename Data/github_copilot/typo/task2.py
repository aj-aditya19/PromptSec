def two_sum(nums, targt):
	seen = {}
	for index, number in enumerate(nums):
		needed = targt - number
		if needed in seen:
			return [seen[needed], index]
		seen[number] = index
	return []
