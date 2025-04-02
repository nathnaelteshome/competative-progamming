from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (right + left) // 2
            print("mis", mid)
 
            if nums[mid] > 0:
                right = mid
            else: 
                left = mid
                
        pos = len(nums) - right

        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (right + left) // 2

            if nums[mid] < 0:
                left = mid
            else: 
                 left = mid


        neg = left + 1


        return max(pos, neg)

        
soln = Solution()
print(soln.maximumCount([-3,-2,-1,0,0,1,2])) # 2