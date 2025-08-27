class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen:
                max_len = max(max_len, right - left)
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1

            else:
                seen.add(s[right])
            # print(word, seen)

        max_len = max(max_len, len(s) - left)

        return max_len
