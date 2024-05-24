import math
from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        if N == 0:
            return 0

        self.toh(N - 1, fromm, aux, to)
        print("move disk", N, "from rod", fromm, "to rod", to)
        self.toh(N - 1, aux, to, fromm)


soln = Solution()
print(soln.toh(4, 1, 3, 2))
