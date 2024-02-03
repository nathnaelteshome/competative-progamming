class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_word = max(len(word1),len(word2))
        output=""
        for word in range (max_word):
            if word < len(word1):
                output += word1[word]
            if word < len(word2):
                output += word2[word]
        return output
    

