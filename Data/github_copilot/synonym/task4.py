def binary_lookup(sorted_values, goal):
	left, right = 0, len(sorted_values) - 1
	while left <= right:
		middle = (left + right) // 2
		if sorted_values[middle] == goal:
			return middle
		if sorted_values[middle] < goal:
			left = middle + 1
		else:
			right = middle - 1
	return -1
