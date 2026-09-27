def count_landmasses(matrix):
    """
    Write a Python method that, given a 2D matrix of '1's (ground) and '0's (sea), 
    returns the count of separate landmasses.
    """
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] == '0':
            return
        matrix[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                dfs(i, j)
                count += 1

    return count
