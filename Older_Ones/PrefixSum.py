from typing import List


class Solution:
    def pivotIndex(self, nums):
        TotalSum = sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == (TotalSum - leftsum - num):
                return i
            leftsum += num
        return -1

# obj = Solution()
# print(obj.pivotIndex(nums=[1, 2, 3, 4, 5, 6, 4]))
