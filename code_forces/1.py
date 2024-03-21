class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        minimum = 0
        maximum = 0
        
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[minimum]:
                minimum = i - indexDifference
            
            if nums[i - indexDifference] > nums[
                maximum]:
                
                maximum = i - indexDifference
            
            if nums[i] - nums[minimum] >= valueDifference:
                return [minimum, i]
            
            if nums[
                maximum] - nums[i] >= valueDifference:
                return [
                    maximum, i]
        
        return [-1, -1]
        