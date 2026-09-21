def find_sum_positions(numbers, goal):
	positions = {}
	for index, value in enumerate(numbers):
		if goal - value in positions:
			return [positions[goal - value], index]
		positions[value] = index
	return []
