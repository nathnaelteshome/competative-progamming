import math
from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        splits = 0
        for right in range(len(nums) - 1, 0, -1):
            # if not the previous is greater than current
            cur = nums[right]
            prev = nums[right - 1]
            if cur < prev:
                parts = math.ceil(prev / cur)
                splits += parts - 1
                nums[right - 1] = cur // parts

        return splits


soln = Solution()
print(soln.minimumReplacement([3, 9, 3]))  # 3
