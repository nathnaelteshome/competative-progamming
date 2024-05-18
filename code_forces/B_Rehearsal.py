from collections import defaultdict


n = int(input())

array = [0]
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    if len(array) < y:
        array += [0] * (y - len(array))
    array[y - 1] += x

maximum = 0
left = 0
right = len(array) - 1

while left < right:

    while array[left] == 0:
        left += 1
    while array[right] == 0:
        right -= 1

    diff = min(array[left], array[right])
    array[left] = array[left] - diff
    array[right] = array[right] - diff

    maximum = max(maximum, (left + right + 2))

print(maximum)
