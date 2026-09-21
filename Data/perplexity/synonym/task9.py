# Prompt:
# Write a Python method that, given a 2D matrix of '1's (ground) and '0's (sea), returns the count of separate landmasses.

# Python solution below

def number_of_islands(grid):
    if not grid:
        return 0
    rows, cols, count = len(grid), len(grid[0]), 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                count += 1
                stack = [(row, col)]
                grid[row][col] = '0'
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            stack.append((nr, nc))
    return count
