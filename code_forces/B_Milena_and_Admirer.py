t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    ans, maxVal = 0, nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        operations = (nums[i] - 1) // maxVal
        ans = ans + operations
        maxVal = nums[i] // (operations + 1)

    print(ans)
