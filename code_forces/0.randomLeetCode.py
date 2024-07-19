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
        idx = sorted(range(m), key=lambda i: monsters[i])
        s = list(accumulate((coins[i] for i in idx), initial=0))
        ans = []
        for h in heroes:
            i = bisect_right(idx, h, key=lambda i: monsters[i])
            ans.append(s[i])
        return ans


soln = Solution()
print(soln.maximumCoins(heroes, monsters, coins))  # Output: [2, 5, 10]
