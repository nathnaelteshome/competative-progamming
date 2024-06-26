from collections import defaultdict


n, s = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

l = 0
freq = defaultdict(int)
good_segments = 0

for r in range(n):
    freq[nums[r]] += 1
    
    while l <= r and len(freq) > s:
        freq[nums[l]] -= 1

        if freq[nums[l]] == 0:
            del freq[nums[l]]
        l += 1
    
    good_segments += r - l + 1



print(good_segments)

