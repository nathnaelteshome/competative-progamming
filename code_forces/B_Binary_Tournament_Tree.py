# backtrack function
def backtrack(l, r, depth):
    if l >= r:
        return

    # find the maximum element in the array
    maxElement = max(arr[l:r])
    maxIndex = arr.index(maxElement)
    depthMap[maxElement] = depth

    # recurse through the left and right subtree
    backtrack(l, maxIndex, depth + 1)
    backtrack(maxIndex + 1, r, depth + 1)


# take input
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    depthMap = {}

    # call backtrack function
    backtrack(0, n, 0)
    print(*[depthMap[x] for x in arr])
