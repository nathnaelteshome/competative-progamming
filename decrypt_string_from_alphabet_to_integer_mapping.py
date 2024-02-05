class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabets = '_abcdefghijklmnopqrstuvwxyz'
        i = len(s) - 1
        output = []

        while i >= 0:
            if s[i] == '#':
                output.append(alphabets[int(s[i - 2: i])])
                i -= 3
            else:
                output.append(alphabets[int(s[i])])
                i -= 1

        output.reverse()
        return "".join(output)
                