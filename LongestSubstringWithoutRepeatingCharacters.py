class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        answer = 0
        for right in range(len(s)):
            if s[right] not in seen:
                answer = max(answer, right-left+1)
            else:
                if seen[s[right]] < left:
                    answer = max(answer, right-left+1)
                else:
                    left = seen[s[right]] + 1
            seen[s[right]] = right
        return answer
