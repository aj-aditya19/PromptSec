def num_islands(grid):
	if not grid or not grid[0]:
		return 0
	rows, columns = len(grid), len(grid[0])
	islands = 0
	def visit(row, column):
		if row < 0 or row >= rows or column < 0 or column >= columns:
			return
		if grid[row][column] != '1':
			return
		grid[row][column] = '0'
		visit(row + 1, column)
		visit(row - 1, column)
		visit(row, column + 1)
		visit(row, column - 1)
	for row in range(rows):
		for column in range(columns):
			if grid[row][column] == '1':
				visit(row, column)
				islands += 1
	return islands
