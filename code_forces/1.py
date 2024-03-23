from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        idxOfMinValue = 0
        idxOfMaxVal = 0
        
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[idxOfMinValue]:
                idxOfMinValue = i - indexDifference
            
            if nums[i - indexDifference] > nums[idxOfMaxVal]:
                
                idxOfMaxVal = i - indexDifference
            
            if nums[i] - nums[idxOfMinValue] >= valueDifference:
                return [idxOfMinValue, i]
            
            if nums[idxOfMaxVal] - nums[i] >= valueDifference:
                return [idxOfMaxVal, i]
        
        return [-1, -1]

soln = Solution()
print(soln.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))