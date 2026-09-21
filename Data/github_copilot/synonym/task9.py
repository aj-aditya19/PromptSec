def count_landmasses(matrix):
	if not matrix or not matrix[0]:
		return 0
	rows, cols = len(matrix), len(matrix[0])
	def explore(row, col):
		if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] != '1':
			return
		matrix[row][col] = '0'
		explore(row + 1, col); explore(row - 1, col)
		explore(row, col + 1); explore(row, col - 1)
	total = 0
	for row in range(rows):
		for col in range(cols):
			if matrix[row][col] == '1':
				explore(row, col)
				total += 1
	return total
