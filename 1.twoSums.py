from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    return ans


# p1 = Solution()
# print(p1.twoSum([2, 7, 11, 15], 20))
