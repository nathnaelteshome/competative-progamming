n = int(input())
nums = [int(x) for x in input().split()]

nums.sort()
index = 0
for idx, num in enumerate(nums):
    if num > 0:
        index = idx
        break


min_odd = min([abs(num) for num in nums if num % 2 == 1])
summation = sum(nums[index:])

if summation % 2 == 0:
    summation -= min_odd

print(summation)
