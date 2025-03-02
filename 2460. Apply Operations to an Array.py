from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *= 2
                nums[i] = 0

        left = 0
        for right in range(n):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


soln = Solution()
print(soln.applyOperations([1, 1, 2, 2]))  # [4, 0, 0, 0]
