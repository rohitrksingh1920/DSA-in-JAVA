class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        
        k %= n
        
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # left shift
                    new_j = (j + k) % n
                else:
                    # right shift
                    new_j = (j - k + n) % n
                
                if mat[i][j] != mat[i][new_j]:
                    return False
        
        return True