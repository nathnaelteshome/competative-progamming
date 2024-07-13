from collections import deque


n = int(input())

for _ in range(n):
    n, m = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    lakes = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                lakes.append((row, col))

    visited = set()

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_volume = 0

    for cell in lakes:
        if cell in visited:
            continue
        queue = deque([cell])
        visited.add(cell)
        volume = matrix[cell[0]][cell[1]]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]

                    if (
                        0 <= new_row < n
                        and 0 <= new_col < m
                        and (new_row, new_col) not in visited
                        and matrix[new_row][new_col] != 0
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        volume += matrix[new_row][new_col]

            max_volume = max(max_volume, volume)
    print(max_volume)
