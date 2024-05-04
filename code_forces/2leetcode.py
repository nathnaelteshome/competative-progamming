
from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n is negative:
        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            negative = True  
        else: 
            negative = False
        return self.myPow(x, abs(n - 1)) * x if not negative else 1 / (self.myPow(x, abs(n - 1)) * x)

soln = Solution()

