class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            l = i - 2
            r = i - 1
            if nums[l] + nums[r] > nums[i]:
                return  nums[l] + nums[r] + nums[i]

        return 0
        