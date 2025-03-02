class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
            left += 1

        pointZero = 0
        for seek in range(len(nums)):
            if nums[seek] != 0:
                nums[pointZero], nums[seek] = nums[seek], nums[pointZero]
                pointZero += 1
        return nums
