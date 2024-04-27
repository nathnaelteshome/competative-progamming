
from collections import defaultdict, deque
from typing import List, Optional


# Definition for singly-linked list.
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()

        left = ans = 0
        for right in range(len(nums)):
            while increasing and increasing[-1] < nums[right]:
                increasing.pop()
            increasing.append(nums[right])
            
            while decreasing and decreasing[-1] > nums[right]:
                decreasing.pop()
            
            decreasing.append(nums[right])

            while abs(decreasing[0] - increasing[0]) > limit:
                if decreasing[0] == nums[left]:
                    decreasing.popleft()
                if increasing[0] == nums[left]:
                    increasing.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans

soln = Solution()
# Create a linked list from the list [1,2,3,4,5]


# Call the function and print the reversed list
nums = [8,2,4,7]
limit = 4
print(soln.longestSubarray(nums, limit))  # Output: 4