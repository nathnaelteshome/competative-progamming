class Solution:
    def reverseWords(self, s: str) -> str:
        output = s.strip().split()
        output.reverse()
        
        return " ".join(output)
        