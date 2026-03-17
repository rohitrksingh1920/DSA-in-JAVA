class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        for row in matrix:
            row.sort(reverse=True)
            
            for j in range(n):
                max_area = max(max_area, row[j] * (j + 1))
        
        return max_area