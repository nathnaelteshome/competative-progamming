n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

nums.sort(reverse=True)


freq = 0

l, r = 0, 0
ans = nums[0]

for r in range(n):
    k -= nums[l] - nums[r]
    while k < 0:
        k += (r - l) * (nums[l] - nums[l + 1])
        l += 1

    if freq <= r - 1 + 1:
        freq = r - l + 1
        ans = nums[l]

print(*[freq, ans])
