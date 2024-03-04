m = int(input())

for _ in range(m):
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    minimum = 10**5

    for index in range(1, n):
        minimum = min(minimum, (nums[index] - nums[index -1]))

    print(minimum)