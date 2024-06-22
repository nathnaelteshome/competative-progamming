n = int(input())

for _ in range(n):
    input()
    nums = [int(x) for x in input().split()]

    current_sum = 0
    for i in range(0, len(nums), 2):
        current_sum += nums[i]

    osprofit = []
    for i in range(1, len(nums), 2):
        osprofit.append(nums[i] - nums[i - 1])

    esprofit = []
    for i in range(2, len(nums), 2):
        esprofit.append(nums[i - 1] - nums[i])

    def kadane(arr):
        ans = 0
        cursum = 0
        for num in arr:
            cursum = max(num, cursum + num)
            ans = max(ans, cursum)

        return ans

    even = kadane(esprofit)
    odd = kadane(osprofit)

    print(max(even, odd) + current_sum)
