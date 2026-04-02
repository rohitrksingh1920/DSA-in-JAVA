class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        

        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # skip (0,0)

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    cur = dp[i][j][k]
                    if cur == -float('inf'):
                        continue
                    
                    for ni, nj in ((i, j+1), (i+1, j)):  # right & down
                        if ni < m and nj < n:
                            val = coins[ni][nj]
                            dp[ni][nj][k] = max(dp[ni][nj][k], cur + val)
                            if val < 0 and k < 2:        # skip the cell
                                dp[ni][nj][k+1] = max(dp[ni][nj][k+1], cur)

        return max(dp[m-1][n-1])