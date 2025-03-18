from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        cur = 0
        left = 0
        max_size = 0

        for right in range(len(nums)):
            while cur & nums[right] != 0:
                cur ^= nums[left]
                left += 1

            cur != nums[right]

            max_size = max(max_size, right - left + 1)

        return max_size


soln = Solution()
print(soln.longestNiceSubarray([1, 3, 8, 48, 10]))
