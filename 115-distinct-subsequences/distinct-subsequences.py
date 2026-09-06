class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)

        dp = [0] * (n + 1)
        dp[0] = 1

        for char in s:
            for j in range(n - 1, -1, -1):
                if char == t[j]:
                    dp[j + 1] += dp[j]

        return dp[n]