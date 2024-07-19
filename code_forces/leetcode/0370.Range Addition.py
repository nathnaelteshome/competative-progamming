from itertools import accumulate
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        d = [0] * length
        for l, r, c in updates:
            d[l] += c
            if r + 1 < length:
                d[r + 1] -= c
        acc = accumulate(d)
        lol = list(acc)
        return lol


soln = Solution()
print(
    soln.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
)  # Output: [-2, 0, 3, 5, 3]
