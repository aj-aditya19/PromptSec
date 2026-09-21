def count_landmasses(matrix):
    if not matrix or not matrix[0]:
        return 0
    num_rows, num_cols = len(matrix), len(matrix[0])
    visited = set()

    def explore(row, col):
        if (row < 0 or row >= num_rows or col < 0 or col >= num_cols
                or (row, col) in visited or matrix[row][col] == '0'):
            return
        visited.add((row, col))
        explore(row+1, col)
        explore(row-1, col)
        explore(row, col+1)
        explore(row, col-1)

    total = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == '1' and (row, col) not in visited:
                explore(row, col)
                total += 1
    return total
