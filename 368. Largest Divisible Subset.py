from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        dp = [[num for num in nums]]

        for i in range(len(nums) - 1, -1, -1):
            max_length = 0
            for j in range(i + 1, len(nums)): 
                temp_length = len(dp[j])
                if nums[j] % nums[i] == 0:
                    if max_length < temp_length:
                        dp[i] = [nums[i]] + dp[j]
                        max_length = temp_length

        
        dp.sort(key = lambda x: len(x))

        return dp[-1]

soln = Solution()
print(soln.largestDivisibleSubset([1, 2, 3]))