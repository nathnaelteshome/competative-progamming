import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        m, n = len(nums1), len(nums2)

        res = []
        hp = []
        for i in range(min(m, k)):
            heapq.heappush(hp, (nums1[i] + nums2[0], i, 0))

        for _ in range(k):
            num, i, j = heapq.heappop(hp)
            res.append((nums1[i], nums2[j]))

            if j + 1 < n:
                heapq.heappush(hp, (nums1[i] + nums2[j + 1], i, j + 1))

        return res


soln = Solution()
print(soln.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 20))
