class Solution {
    public int largestMagicSquare(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        // Prefix sums
        int[][] row = new int[m][n + 1];
        int[][] col = new int[m + 1][n];
        int[][] diag1 = new int[m + 1][n + 1];
        int[][] diag2 = new int[m + 1][n + 1];

        // Build prefix sums
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row[i][j + 1] = row[i][j] + grid[i][j];
                col[i + 1][j] = col[i][j] + grid[i][j];
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j];
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j];
            }
        }

        // Try largest size first
        for (int size = Math.min(m, n); size >= 2; size--) {
            for (int i = 0; i + size <= m; i++) {
                for (int j = 0; j + size <= n; j++) {

                    int target = row[i][j + size] - row[i][j];
                    boolean ok = true;

                    // Check rows
                    for (int r = i; r < i + size && ok; r++) {
                        if (row[r][j + size] - row[r][j] != target)
                            ok = false;
                    }

                    // Check columns
                    for (int c = j; c < j + size && ok; c++) {
                        if (col[i + size][c] - col[i][c] != target)
                            ok = false;
                    }

                    // Check diagonals
                    int d1 = diag1[i + size][j + size] - diag1[i][j];
                    int d2 = diag2[i + size][j] - diag2[i][j + size];

                    if (ok && d1 == target && d2 == target)
                        return size;
                }
            }
        }
        return 1;
    }
}
