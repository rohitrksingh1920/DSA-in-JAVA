class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [1] + [0] * (n - 1)

        for i in range(m):
            left = 0

            for j in range(n):
                if grid[i][j] == 1:
                    left, dp[j] = dp[j], left
                else:
                    left = (left + dp[j]) % MOD
                    dp[j] = left

        return left
