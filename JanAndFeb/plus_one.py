class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""

        for digit in digits:
            string += str(digit)

        result = [int(i) for i in str(int(string) + 1)]
        
        return result
        