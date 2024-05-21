n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

nums.sort(reverse=True)  # 6 4 3 2 0


maxWindow = 0

l = 0
ans = nums[0]  # 6

for r in range(n):
    k -= nums[l] - nums[r]
    while k < 0:
        k += (r - l) * (nums[l] - nums[l + 1])
        l += 1

    if maxWindow <= r - l + 1:
        maxWindow = r - l + 1
        ans = nums[l]

print(*[maxWindow, ans])
