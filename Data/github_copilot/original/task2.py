def two_sum(nums, target):
	positions = {}
	for index, number in enumerate(nums):
		complement = target - number
		if complement in positions:
			return [positions[complement], index]
		positions[number] = index
	return []
