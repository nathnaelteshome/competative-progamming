from typing import Counter


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = 0
        if Counter(goal) != Counter(s): return False


        while l < len(s):
            r = 0
            ans = 0
            while s[l % len(s)] == goal[r]:
                ans += 1
                l += 1
                r += 1
                if ans == len(goal):
                    return True

            if l != 0 and r!= 0 and s[l % len(s) - 1] == goal[r - 1]:continue
            l += 1
        return False

soln = Solution()
soln.rotateString("defdefdefabcabc","defdefabcabcdef")


