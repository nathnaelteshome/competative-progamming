from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, first, last):
            while first <= last:
                nums[first], nums[last] = nums[last], nums[first]
                first += 1
                last -= 1

        last = len(nums)-1
        k = k % (last+1)
        reverse(nums, 0, last-k)
        reverse(nums, last-k + 1, last)
        reverse(nums, 0, last)


# obj = Solution()
# print(obj.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
