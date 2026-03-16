class Solution {
    public int find(int[][] grid , int i , int j , int k ) {

        int n = grid.length;
        int m = grid[0].length;

        if (i + 2 * k >= n || j + k >= m || j - k < 0) return -1;

        int r = i;
        int c = j;
        int sum = 0;

        for (int l = 0; l < k; l++) {
            sum += grid[r + l][c - l];
        }

        r = i + k;
        c = j - k;

        for (int l = 0; l < k; l++) {
            sum += grid[r + l][c + l];
        }

        r = i + 2 * k;
        c = j;

        for (int l = 0; l < k; l++) {
            sum += grid[r - l][c + l];
        }

        r = i + k;
        c = j + k;

        for (int l = 0; l < k; l++) {
            sum += grid[r - l][c - l];
        }

        return sum;
    }

    public int[] getBiggestThree(int[][] grid) {

        int row = grid.length;
        int col = grid[0].length;

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {

                if (set.add(grid[i][j])) {
                    pq.add(grid[i][j]);
                    if (pq.size() > 3) pq.remove();
                }

                for (int k = 1; k < (Math.min(row, col) / 2) + 1; k++) {

                    int val = find(grid, i, j, k);

                    if (val == -1) break;

                    if (set.add(val)) {
                        pq.add(val);
                        if (pq.size() > 3) pq.remove();
                    }
                }
            }
        }

        int n = pq.size();
        int[] ans = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            ans[i] = pq.remove();
        }

        return ans;
    }
}