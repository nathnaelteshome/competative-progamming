class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rowLength = len(matrix)
        colLength = len(matrix[0])
        transposeMatrix = [[0] * rowLength for _ in range(colLength)]
        
        for row in range(rowLength):
            for col in range(colLength):
                transposeMatrix[col][row] = matrix[row][col]
        
        return transposeMatrix
