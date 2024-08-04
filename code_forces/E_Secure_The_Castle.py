directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]


def block_bad(grid, row, col, visited):
    stack = [(row, col)]
    visited[row][col] = True

    while stack:
        x, y = stack.pop()

        for dx, dy in directions:
            new_row, new_col = x + dx, y + dy
            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])
                and not visited[new_row][new_col]
            ):
                if grid[new_row][new_col] == ".":
                    grid[new_row][new_col] = "#"
                elif grid[new_row][new_col] != "#":
                    stack.append((new_row, new_col))
                    visited[new_row][new_col] = True


def can_exit(grid, row, col, visited):
    stack = [(row, col)]
    visited[row][col] = True
    flag = False

    while stack:
        x, y = stack.pop()

        if (x == len(grid) - 1) and (y == len(grid[0]) - 1):
            flag = True

        for dx, dy in directions:
            new_row, new_col = x + dx, y + dy
            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])
                and not visited[new_row][new_col]
                and grid[new_row][new_col] != "#"
            ):
                stack.append((new_row, new_col))
                visited[new_row][new_col] = True

    return flag


def solve():
    n, m = map(int, input().split())

    grid = [0] * n

    for i in range(n):
        grid[i] = list(input().strip())

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "B" and not visited[i][j]:
                block_bad(grid, i, j, visited)

    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (
                grid[i][j] == "G"
                and not visited[i][j]
                and not can_exit(grid, i, j, visited)
            ):
                print("No")
                return

    print("Yes")


t = int(input())
for _ in range(t):
    solve()
