from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        incr = deque()  # increasing monotonic queue
        dec = deque()  # decreasing monotonic queue
        l = 0
        ans = 0


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        left, right = 1, 2 ** (n - 1)

        for _ in range(n - 1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                cur = 0 if cur == 1 else 1

        return cur


soln = Solution()
print(soln.kthGrammar(4, 5))  # 1
