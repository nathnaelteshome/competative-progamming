from collections import defaultdict


n = int(input())

matrix = [[int(x) for x in input().split()] for x in range(n)]
count = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 1:
            count += 1

print(count // 2)
