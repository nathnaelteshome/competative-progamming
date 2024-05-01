
from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n % 3 != 0:
            return n == 1 # checks if last recurssion has a value 1
        else:
            return self.isPowerOfThree(n/3)

soln = Solution()

print(soln.isPowerOfThree(27)) # True
print(soln.isPowerOfThree(0)) # False
print(soln.isPowerOfThree(45)) # False