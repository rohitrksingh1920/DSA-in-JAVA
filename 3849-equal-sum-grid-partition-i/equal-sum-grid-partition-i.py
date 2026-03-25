class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Total sum of grid
        total = sum(sum(row) for row in grid)
        
        # Check horizontal cuts
        curr_sum = 0
        for i in range(m - 1):
            curr_sum += sum(grid[i])
            if curr_sum == total - curr_sum:
                return True
        
        # Check vertical cuts
        curr_sum = [0] * n
        for i in range(m):
            for j in range(n):
                curr_sum[j] += grid[i][j]
        
        prefix = 0
        for j in range(n - 1):
            prefix += curr_sum[j]
            if prefix == total - prefix:
                return True
        
        return False