from itertools import accumulate
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_val = 0
        cumSum = 0
        delta = [0] * 1000010
        for start, end in intervals:
            delta[start] += 1
            delta[end] -= 1
        for num in delta:
            cumSum += num
            max_val = max(max_val, cumSum)
        return max_val


soln = Solution()
print(soln.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # Output: 2
