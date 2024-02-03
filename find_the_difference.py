class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        for letter in count_t.keys():
            if letter not in count_s.keys() or count_s[letter] != count_t[letter]:
                return letter
