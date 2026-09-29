class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid path must have an even number of cells
        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, balance):
            if i >= m or j >= n:
                return False

            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            remaining = (m - 1 - i) + (n - 1 - j)

            if balance > remaining:
                return False

            if (balance - remaining) % 2 != 0:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            return (
                dfs(i + 1, j, balance) or
                dfs(i, j + 1, balance)
            )

        return dfs(0, 0, 0)