def count_connected_land_groups(grid):
    """
    Create a function in Python that scans a 2D grid of land and water cells 
    and counts how many separate, connected groups of land cells exist.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count
