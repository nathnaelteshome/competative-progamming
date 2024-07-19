from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        idx = 0

        while miss <= n: #1 <= 20
            # if the missing number is not what we're pointing at iit is  equal or bigger
            if idx < len(nums) and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            # if we dont have the missing number in the list
            else:
                miss += miss
                result += 1

        return result

soln = Solution()
print(soln.minPatches([1,5,10 ,11,25,100], 200))  # Output: 1