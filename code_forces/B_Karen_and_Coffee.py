N = 200005
 
n, k, q = map(int, input().split())
 
arr = [0] * N
 
for _ in range(n):
    left, right = map(int, input().split())
    arr[left] += 1
    arr[right + 1] -= 1
 
count = 0
for i in range(len(arr)):
    count += arr[i]
    arr[i] = 1 if count >= k else 0
 
p = [0] * N
for i in range(1, len(p)):
    p[i] = arr[i - 1] + p[i - 1]
 
for _ in range(q):
    left, right = map(int, input().split())
    print(p[right + 1] - p[left])