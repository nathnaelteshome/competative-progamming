class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rowLength = len(strs)
        colLength = len(strs[0])
        result = 0
        
        for col in range(colLength):
            arr = []
            for row in range(rowLength):
                if arr and strs[row][col] < arr[-1]:
                    result += 1
                    break
                arr.append(strs[row][col])

        return result