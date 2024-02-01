from typing import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq = sorted(list(counter.values()))

        max_idle = freq.pop()
        total = (max_idle-1)*n

        while freq and total > 0:
            total = total-min(max_idle-1, freq.pop())

        total = max(0, total)
        return len(tasks) + total


# obj = Solution()
# print(obj.leastInterval([4, 4, 45, 45, 45, 76, 876,
#       76, 56, 76, 76, 76, 76, 56, 56, 45, 76, 876, ], 4))
