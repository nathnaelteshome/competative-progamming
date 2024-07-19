from typing import List


class Solution:
    # Similar to 1950. Maximum of Minimum Values in All Subarrays
    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        # prevMin[i] := the index k s.t.
        # nums[k] is the previous minimum in nums[0..n)
        prevMin = [-1] * n
        # nextMin[i] := the index k s.t.
        # nums[k] is the next minimum innums[i + 1..n)
        nextMin = [n] * n
        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                nextMin[index] = i
            if stack:
                prevMin[i] = stack[-1]
            stack.append(i)

        # For each nums[i], let l = nextMin[i] + 1 and r = nextMin[i] - 1.
        # nums[i] is the minimun in nums[l..r].
        # So, the ans[r - l + 1] will be at least nums[i].
        for num, l, r in zip(nums, prevMin, nextMin):
            sz = r - l - 1
            ans[sz - 1] = max(ans[sz - 1], num)

        # ans[i] should always >= ans[i + 1..n).
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i], ans[i + 1])

        return ans


soln = Solution()
print(soln.findMaximums([2, 1, 2, 100, 105, 89]))

print(sorted([2, 1, 2, 100, 89, 3, 6, 6, 2, -3, 1, 4, 6, 78, 2, 9, 5, 7, 3]))
