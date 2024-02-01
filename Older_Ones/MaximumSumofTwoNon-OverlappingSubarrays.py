class Solution:
    def maxSumTwoNoOverlap(self, nums, first: int, sec: int) -> int:
        maxSum = 0
        index1, index2 = 0, 0
        mx1, mx2 = 0, 0
        while index1 < len(nums) - first + 1:
            mx1 = sum(nums[index1:index1 + first])
            if sec <= index1:
                index2 = 0
                while index2 + sec <= index1:
                    mx2 = sum(nums[index2:index2 + sec])
                    maxSum = max(maxSum, mx1 + mx2)
                    index2 += 1

            if len(nums) - (index1 + 1) >= sec:
                index2 = 0
                while index2 + index1 + sec <= len(nums):
                    mx2 = sum(
                        nums[index1 + index2 + first:index1 + index2 + first + sec])
                    maxSum = max(maxSum, mx1 + mx2)
                    index2 += 1
            index1 += 1
        return maxSum
