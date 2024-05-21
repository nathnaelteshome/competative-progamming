from collections import defaultdict, deque
import math
from typing import List, Optional


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: list) -> int:
        # search for peak
        left, right = -1, len(mountain_arr)

        while left + 1 < right:
            mid = (right + left) // 2

            middle = mountain_arr[mid]
            next_middle = mountain_arr[mid + 1]
            if middle < next_middle:
                left = mid
            else:
                right = mid

        peak = right

        left = -1
        right = peak + 1

        # find target in the increasing side
        while left + 1 < right:
            mid = (right + left) // 2
            middle = mountain_arr[mid]
            next_middle = mountain_arr[mid + 1]

            if middle < next_middle:
                left = mid
            else:
                right = mid

        if mountain_arr[(mid)] == mountain_arr[(target)]:
            ans = mid
        print(mid)

        # find in the decreasing
        left = peak - 1
        right = len(mountain_arr)
        while left < right:
            mid = (right + left) // 2
            if mountain_arr[(mid)] > mountain_arr[(target)]:
                left = mid
            elif mountain_arr[(mid)] == mountain_arr[(target)]:
                return mid
            else:
                right = mid

        return -1


soln = Solution()
print(soln.findInMountainArray(3, [1, 2, 3, 4, 5, 3, 1]))

a = b = 0
no_of_stones = input()
for i in input():
    a += b == i
    b = i
print(a)
