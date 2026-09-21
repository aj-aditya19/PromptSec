def count_connected_land_groups(grid):
    if not grid:
        return 0
    n_rows = len(grid)
    n_cols = len(grid[0])

    def flood_fill(r, c):
        if r < 0 or r >= n_rows or c < 0 or c >= n_cols:
            return
        if grid[r][c] != '1':
            return
        grid[r][c] = '#'
        flood_fill(r+1, c)
        flood_fill(r-1, c)
        flood_fill(r, c+1)
        flood_fill(r, c-1)

    groups = 0
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == '1':
                flood_fill(r, c)
                groups += 1
    return groups
