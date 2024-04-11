n, x = [int(x) for x in input().split()]
arr = [0] + [int(x) for x in input().split()]

running_sum = 0
def findBounce(arr, x):
    running_sum = 0
    
    if arr[1] >= x:
        return 1

    for idx in range(n):
        
        running_sum += arr[idx]

        if running_sum == x:
            return idx + 1
            

        elif running_sum > x:
            return idx
    
    return 1

print(findBounce(arr, x))
