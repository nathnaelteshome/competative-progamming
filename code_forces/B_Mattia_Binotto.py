n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

prefix_sum = [0] * n
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

satisfied = n

for i in range(1, n):
    if arr[i] < prefix_sum[i-1]:
        satisfied -= 1

print(satisfied)  # Fix: Add parentheses to the print statement


