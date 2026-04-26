class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.m, self.n = len(grid), len(grid[0])
        visited = [[False] * self.n for _ in range(self.m)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, prev_r, prev_c):
            if visited[r][c]:
                return True
            
            visited[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < self.m and 0 <= nc < self.n and
                    grid[nr][nc] == grid[r][c]):
                    
                    if nr == prev_r and nc == prev_c:
                        continue
                    
                    if dfs(nr, nc, r, c):
                        return True
            
            return False
        
        for i in range(self.m):
            for j in range(self.n):
                if not visited[i][j]:
                    if dfs(i, j, i, j):
                        return True
        
        return False