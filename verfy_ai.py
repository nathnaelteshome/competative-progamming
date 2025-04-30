import heapq
from collections import defaultdict


def maxSumPairs(nums):
    groups = defaultdict(
        list
    )  # key = max_digit, value = group of num that have similar max digit
    max_value = -1

    for num in nums:
        stringified_num = str(num)
        key = max([int(digit) for digit in stringified_num])
        heapq.heappush(groups[key], -num)

    for group in groups.values():
        if len(group) >= 2:
            first = -heapq.heappop(group)
            second = -heapq.heappop(group)
            max_value = max(max_value, first + second)

    return max_value


print(maxSumPairs([51, 71, 17, 42]))  # Expected output: 93
print(maxSumPairs([1, 2, 3, 4]))  # Expected output: -1
print(maxSumPairs([1, 2, 3, 4, 5, 6]))  # Expected output: -1
print(maxSumPairs([2536, 1613, 71, 7610, 73, 3366, 162]))  # Output: 5902
print(maxSumPairs([112, 131, 411]))  # Output: -1
