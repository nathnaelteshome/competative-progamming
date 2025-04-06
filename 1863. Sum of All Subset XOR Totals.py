from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all_sub = []

        def backtrack(subset, i):
            if i == len(nums):
                all_sub.append(subset)
                return

            backtrack(subset + [nums[i]], i + 1)
            backtrack(subset, i + 1)

        backtrack([], 0)

        result = 0
        for sub_set in all_sub:
            temp = 0
            for num in sub_set:
                temp ^= num
            result += temp

        return result

soln = Solution()
print(soln.subsetXORSum([5, 1, 6]))