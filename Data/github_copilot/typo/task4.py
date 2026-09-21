def binary_search(arr, targt):
	low, high = 0, len(arr) - 1
	while low <= high:
		middle = (low + high) // 2
		if arr[middle] == targt:
			return middle
		if arr[middle] < targt:
			low = middle + 1
		else:
			high = middle - 1
	return -1
