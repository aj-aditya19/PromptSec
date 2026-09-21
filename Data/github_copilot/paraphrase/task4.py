def locate_value(sorted_values, value):
	start, end = 0, len(sorted_values) - 1
	while start <= end:
		middle = (start + end) // 2
		if sorted_values[middle] == value:
			return middle
		if sorted_values[middle] < value:
			start = middle + 1
		else:
			end = middle - 1
	return -1
