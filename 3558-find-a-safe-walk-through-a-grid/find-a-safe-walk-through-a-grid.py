class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        start = health - grid[0][0]
        if start <= 0:
            return False

        # best[i][j] = maximum health left when reaching (i, j)
        best = [[-1] * n for _ in range(m)]
        best[0][0] = start

        q = deque([(0, 0, start)])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y, h = q.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]

                    if nh > 0 and nh > best[nx][ny]:
                        best[nx][ny] = nh
                        q.append((nx, ny, nh))

        return False