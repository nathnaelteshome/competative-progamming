n = input().split()
nums = [int(x) for x in input().split()]

nums.sort()
l, r = 0, len(nums) - 1
result = []

while l < r:
    result.append(nums[l])
    result.append(nums[r])
    l += 1
    r -= 1

if l == r:
    result.append(nums[l])

print(*result)