class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])

        nums = []
        for row in grid:
            nums.extend(row)

        size = n * m

        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * nums[i - 1]) % MOD

        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * nums[i + 1]) % MOD

        result = []
        for i in range(size):
            result.append((prefix[i] * suffix[i]) % MOD)

        ans = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(result[idx])
                idx += 1
            ans.append(row)
        
        return ans