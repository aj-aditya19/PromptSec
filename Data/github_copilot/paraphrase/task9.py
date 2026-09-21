def count_connected_groups(grid):
	if not grid or not grid[0]:
		return 0
	rows, cols = len(grid), len(grid[0])
	def mark(row, col):
		if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
			return
		grid[row][col] = '0'
		mark(row + 1, col); mark(row - 1, col)
		mark(row, col + 1); mark(row, col - 1)
	groups = 0
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == '1':
				mark(row, col)
				groups += 1
	return groups
