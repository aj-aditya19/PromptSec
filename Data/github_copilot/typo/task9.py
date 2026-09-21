def num_islands(grid):
	if not grid or not grid[0]:
		return 0
	rows, cols = len(grid), len(grid[0])
	def flood(row, col):
		if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
			return
		grid[row][col] = '0'
		flood(row + 1, col); flood(row - 1, col)
		flood(row, col + 1); flood(row, col - 1)
	count = 0
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == '1':
				flood(row, col)
				count += 1
	return count
