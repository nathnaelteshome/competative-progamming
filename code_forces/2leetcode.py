from collections import defaultdict, deque
import math
from typing import List, Optional


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if arr[mid] < arr[right]:
                left = mid
            else:
                right = mid

        return right


soln = Solution()
print(soln.peakIndexInMountainArray(arr=[3, 4, 5, 1]))  # 1

a = b = 0
no_of_stones = input()
for i in input():
    a += b == i
    b = i
print(a)
