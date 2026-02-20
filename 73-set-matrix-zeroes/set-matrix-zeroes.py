class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        temp = [row[:] for row in matrix]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for k in range(cols):
                        temp[i][k] = 0
                    
                    for k in range(rows):
                        temp[k][j] = 0

        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = temp[i][j]