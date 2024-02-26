n, m = [int(x) for x in input().split()]
matrix = []
zeroMatrix = [[0 for i in range(m)] for j in range(n)]

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

result = []

for i in range(n - 1):
    for j in range(m - 1):
        if matrix[i][j] == 1 and matrix[i + 1][j] == 1 and matrix[i][j + 1] == 1 and matrix[i + 1][j + 1] == 1:
            zeroMatrix[i][j] = 1
            zeroMatrix[i+1][j] = 1
            zeroMatrix[i][j+1] = 1
            zeroMatrix[i+1][j+1] = 1
            result.append((i + 1, j + 1))

if matrix == zeroMatrix:
    print(len(result))
    for x, y in result:
        print(x, y)

else:
    print(-1)