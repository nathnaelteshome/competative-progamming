n = int(input())
arr = [int(x) for x in input().split()]       #5 2 5 1 4
sortedArr = sorted(arr)                       #1 2 4 5 5
num_of_swaps = 0
results = []

for idx, num in enumerate(arr):
    if arr[idx] == sortedArr[idx]:
        continue

    else:
        swapper = arr.index(sortedArr[idx]) 
        arr[swapper], arr[idx] = arr[idx], arr[swapper]
        num_of_swaps += 1
        results.append([idx, swapper])
        arr[idx] == 10 ** 10

print(num_of_swaps)

for res in results:
    print(*res)





