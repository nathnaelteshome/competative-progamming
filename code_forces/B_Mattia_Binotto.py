n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

stack = [[arr[0], 0]] # [[num, queueTime]]
satisfied = len(arr)

for num in arr[1:]:
    #append to stack with [num, queueTime]
    stack.append([num, stack[-1][1] + stack[-1][0]])
    if num < stack[-1][1]:
        satisfied -= 1

print(satisfied)

