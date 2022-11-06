class Solution:
    def sortSentence(self, s: str) -> str:

        split_array = s.split(" ")

        sorted_word = sorted(split_array, key=lambda w: w[-1])

        word = [w[:-1] for w in sorted_word]

        return " ".join(word)


# obj = Solution()
# print(obj.sortSentence(s="is2 sentence4 This1 a3"))
