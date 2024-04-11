from collections import defaultdict


n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

l = 0
freq = defaultdict(int)
res = 0
segment = 0

for r in range(n):
    freq[nums[r]] += 1
    
    while l <= r and freq and  freq[nums[r]] >= k:
        segment += n - r
        freq[nums[l]] -= 1
        l += 1

print(segment)


    