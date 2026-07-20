class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        total = n * m
        k %= total

        ans = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                newPos = (i * m + j + k) % total
                ans[newPos // m][newPos % m] = grid[i][j]

        return ans