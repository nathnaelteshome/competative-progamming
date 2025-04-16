def max_score(grid):
    m, n = len(grid), len(grid[0])
    max_grid = [[float("-inf")] * n for _ in range(m)]
    res = float("-inf")

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            current_max = float("-inf")

            if i + 1 < m:
                current_max = max(current_max, max_grid[i + 1][j])
            if j + 1 < n:
                current_max = max(current_max, max_grid[i][j + 1])

            if current_max != float("-inf"):
                potential_score = current_max - grid[i][j]
                res = max(res, potential_score)

            max_grid[i][j] = max(grid[i][j], current_max)

    return res

max_score(grid = [
    [10, 3, 6, 4],
    [5, 11, 2, 9],
    [7, 8, 15, 2],
    [4, 6, 5, 11]
])