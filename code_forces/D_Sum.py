
n = int(input())

for _ in range(n):
    size, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    nums.sort()

    right = len(nums) - 1
    left = 0
    
    while k and size and right > left:
        if nums[right] < (nums[left] + nums[left + 1]):
            right -= 1
            size -= 1
        else:
            left += 2
            size -= 2
        k -= 1

    if nums[left: right + 1]:
        print(sum(nums[left: right + 1]))
    else:
        print(0)