# User function Template for python3

# Input: heroes = [1,4,2], monsters = [1,1,5,2,3], coins = [2,3,4,5,6]
from bisect import bisect_right
from itertools import accumulate
from typing import List


heroes = [1, 4, 2]
monsters = [1, 1, 5, 2, 3]
coins = [2, 3, 4, 5, 6]


class Solution:
    def maximumCoins(
        self, heroes: List[int], monsters: List[int], coins: List[int]
    ) -> List[int]:
        m = len(monsters)
        prefix_coin = [0] * (m + 1)
        for idx in range(len(coins)):
            prefix_coin[idx + 1] = prefix_coin[idx] + coins[idx]
        print(prefix_coin)

        idx = sorted(range(m), key=lambda i: monsters[i])
        s = list(accumulate((coins[i] for i in idx), initial=0))
        ans = []
        for h in heroes:
            i = bisect_right(idx, h, key=lambda i: monsters[i])
            ans.append(s[i])
        return ans


# nums = [6, 7, 8, 9, 10, 78]
# target = 6


# def upper_bound(left, right):
#     # left ,right = -1, len(nums)
#     while left + 1 < right:
#         mid = (left + right) // 2

#         if nums[mid] <= target:
#             left = mid
#         else:
#             right = mid

#     if left > -1 and nums[left] != target or left == -1:
#         return -1
#     return left


# upper_bound(-1, len(nums))
soln = Solution()
print(soln.maximumCoins(heroes, monsters, coins))  # Output: [2, 5, 10]
