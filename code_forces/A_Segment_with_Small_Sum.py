n, s =[int(x) for x in input().split()]
array  = [int(x) for x in input().split()]

windowSum = 0
ans = 0
left = 0

for right in range(n):
    windowSum += array[right]
    while left <= right and windowSum > s:
        windowSum -= array[left]
        left += 1
        
    ans = max(right + 1 - left, ans)

print(ans)
        