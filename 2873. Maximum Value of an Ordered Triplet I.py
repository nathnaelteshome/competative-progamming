from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            k = len(nums) - 1
            j = i + 1
            min_val, max_val = nums[j], nums[k]

            while j < k:
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[k])
                j += 1
                k-= 1

            res = max(res, ((nums[i] - min_val )* max_val))
        
        return res 

soln = Solution()
print(soln.maximumTripletValue([18,15,8,13,10,9,17,10,2,16,17]))