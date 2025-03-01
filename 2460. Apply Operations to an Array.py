class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []

        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *= 2
                nums[i] = 0

        left = 0
        for right in range(n):
            while left < n and nums[left]:
                left += 1
            if nums[right] and left < n:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums
