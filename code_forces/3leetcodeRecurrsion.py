import math
from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result


soln = Solution()
print(soln.permute([1, 2, 3]))
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         combination = []

#         def backtrack(num, curr):
#             if len(curr) == k:
#                 combination.append(curr[:])
#                 return

#             for idx in range(num, n + 1):
#                 curr.append(idx)
#                 backtrack(idx + 1, curr)
#                 curr.pop()

#         backtrack(1, [])
#         return combination


# soln = Solution()
# print(soln.combine(4, 2))
