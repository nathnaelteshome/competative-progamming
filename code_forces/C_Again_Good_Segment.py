from collections import defaultdict


n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

l = 0
freq = defaultdict(int)
res = 1
segment = 0

for r in range(n):
    freq[nums[r]] += 1
    if freq and max(freq.values()) >= k:
        segment += 1

    while l <= r and freq and  max(freq.values()) >= k:
        freq[nums[l]] -= 1
        if freq[nums[l]] == 0:
            del freq[nums[l]]
        l += 1

        if freq and max(freq.values()) >= k:
            segment += 1
            if r != n - 1:
                segment += l

        else:
            l -= 1
            freq[nums[l]] += 1
            break

print(segment)


    