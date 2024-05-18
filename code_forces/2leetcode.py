from collections import defaultdict, deque
import math
from typing import List, Optional


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_sort = sorted(intervals, key=lambda x: x[0])
        end_sort = sorted(intervals, key=lambda x: x[1])
        hashMap = {intervals[idx][0]: idx for idx in range(len(intervals))}
        hashMap2 = {}
        ans = []

        for end in end_sort:
            left = -1
            right = len(intervals)

            while left + 1 < right:
                mid = (left + right) // 2
                if start_sort[mid][0] < end[1]:
                    left = mid
                else:
                    right = mid

            if right < len(intervals):
                hashMap2[end[0]] = hashMap[start_sort[right][0]]
            else:
                left = left - 1

        for interval in intervals:
            if interval[0] in hashMap2:
                ans.append(hashMap2[interval[0]])
            else:
                ans.append(-1)

        return ans


soln = Solution()
print(soln.findRightInterval([[3, 4], [2, 3], [1, 2]]))

a = b = 0
no_of_stones = input()
for i in input():
    a += b == i
    b = i
print(a)
