from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        circle = colors + colors[: k - 1]  # [0,1,0,1,0] + [0, 1]
        ans = 0
        count = 1
        for right in range(1, len(circle)):
            if circle[right] == circle[right - 1]:
                count = 1

            else:
                count += 1

            if count == k:
                ans += 1

        return ans


soln = Solution()
print(soln.numberOfAlternatingGroups([0, 1, 0, 1, 0], 3))  # 2
