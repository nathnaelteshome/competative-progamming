n , k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

sliding_window = sum(nums[:k])
min_sum = sliding_window
ans = 1

for idx in range(n - k):
    sliding_window = sliding_window - nums[idx] + nums[idx + k]
    if sliding_window < min_sum:
        min_sum = sliding_window
        ans = idx + 2

print(ans)
