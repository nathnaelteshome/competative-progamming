from typing import List
from math import ceil


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        min_val = float("inf")
        ans = [-1, -1]
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False

        for i in range(2, ceil(right ** (0.5)) + 1):
            if primes[i]:
                for j in range(i * i, right + 1, i):
                    primes[j] = False

        print(primes)

        for number in range(left, right + 1):
            if primes[number]:
                if max(ans) == -1:
                    ans = [number, -float("inf")]
                elif abs(number - max(ans)) < min_val:
                    min_val = number - max(ans)
                    ans = [max(ans), number]

        return ans if float("-inf") not in ans else [-1, -1]


soln = Solution()
print(soln.closestPrimes(19, 31))
