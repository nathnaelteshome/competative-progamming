class Solution:
    def longestOnes(self, nums, k):
        left, mx = 0, 0

        for right, num in enumerate(nums):
            k -= (1-num)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            mx = max(mx, right - left + 1)
        return mx


# obj = Solution()
# print(obj.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
