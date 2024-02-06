class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0

        for num in nums:
            if num == 1:
                ones += 1
                max_ones = max(max_ones, ones)
            else:
                ones = 0

        return max_ones


