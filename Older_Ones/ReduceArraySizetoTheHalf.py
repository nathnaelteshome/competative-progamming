from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        count = Counter(arr)
        frequency = sorted(count.values(), reverse=True)
        half_size = len(arr) // 2
        ans = 0

        while half_size > 0:
            half_size -= frequency[ans]
            ans += 1

        return ans
