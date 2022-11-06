from typing import List


class Solution:
    def numRescueoutput(self, people: List[int], limit: int) -> int:
        people.sort()
        first = 0
        last = len(people)-1
        output = 0
        while first <= last:
            if people[first] + people[last] <= limit:
                first += 1
                last -= 1
            else:
                last -= 1
            output += 1
        return output


# obj = Solution()
# print(obj.numRescueoutput(people=[1, 1, 2, 3, 9, 10, 11, 12], limit=12))
