class Solution {
    public int[][] generateMatrix(int n) {
        int[][] arr = new int[n][n];
        int count = 1;

        int minRow = 0;
        int maxRow = n - 1;
        int minCol = 0; 
        int maxCol = n - 1;

        while (count <= n * n) {

            for (int c = minCol; c <= maxCol; c++) {
                arr[minRow][c] = count++;
            }

            for (int r = minRow + 1; r <= maxRow; r++) {
                arr[r][maxCol] = count++;
            }

            if (minRow < maxRow) {
                for (int c = maxCol - 1; c >= minCol; c--) {
                    arr[maxRow][c] = count++;
                }
            }

            if (minCol < maxCol) {
                for (int r = maxRow - 1; r > minRow; r--) {
                    arr[r][minCol] = count++;
                }
            }

            minRow++;
            maxRow--;
            minCol++;
            maxCol--;
        }

        return arr;
    }
}
