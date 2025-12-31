class Solution {
    int[] dir = {0, 1, 0, -1, 0};

    public int latestDayToCross(int row, int col, int[][] cells) {
        int left = 1;
        int right = row * col; 
        int ans = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canCross(row, col, cells, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    private boolean canCross(int row, int col, int[][] cells, int day) {
        boolean[][] grid = new boolean[row][col];

        for (int i = 0; i < day; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = true;
        }

        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[row][col];

        for (int j = 0; j < col; j++) {
            if (!grid[0][j]) {
                q.offer(new int[]{0, j});
                visited[0][j] = true;
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];

            if (r == row - 1) return true;

            for (int d = 0; d < 4; d++) {
                int nr = r + dir[d], nc = c + dir[d + 1];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col
                        && !grid[nr][nc] && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc});
                }
            }
        }
        return false;
    }
}
