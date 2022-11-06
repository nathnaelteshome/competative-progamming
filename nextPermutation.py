from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, l, h):
            while l < h:
                arr[l], arr[h] = arr[h], arr[l]
                l += 1
                h -= 1

        pivot = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
        else:
            for i in range(len(nums)-1, pivot-1, -1):
                if nums[pivot-1] < nums[i]:
                    nums[pivot-1], nums[i] = nums[i], nums[pivot-1]
                    break
            first = pivot
            last = len(nums)-1

            reverse(nums, first, last)


# obj = Solution()
# print(obj.nextPermutation(nums=[3, 2, 1]))
