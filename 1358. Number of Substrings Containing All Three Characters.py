from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] +=1

            while len(count) == 3:
                ans += len(s) - right
                count[s[left]] -= 1
                left += 1
                del count[s[left]]
            
        return ans 

soln = Solution()
print(soln.numberOfSubstrings("abcabc")) # 10