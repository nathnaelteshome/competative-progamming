from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        ans = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start

        return ans


sonl = Solution()
print(sonl.countSubarrays([1, 3, 2, 3, 3], 2))  # Output: 0
