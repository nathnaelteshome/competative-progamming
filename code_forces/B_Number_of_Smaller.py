n, m = [int(x) for x in input().split()]
array1 = [int(x) for x in input().split()]
array2 = [int(x) for x in input().split()]
result = []

for num in array2:
    first = 0

    while first < len(array1) and array1[first] < num:
        first += 1

    result.append(first)

print(*result)