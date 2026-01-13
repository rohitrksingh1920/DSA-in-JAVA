class Solution {
    public double separateSquares(int[][] squares) {
        double low = Double.MAX_VALUE;
        double high = Double.MIN_VALUE;

        // Determine search range
        for (int[] sq : squares) {
            low = Math.min(low, sq[1]);
            high = Math.max(high, sq[1] + sq[2]);
        }

        // Binary search for the y-coordinate
        for (int i = 0; i < 60; i++) { // enough for precision
            double mid = (low + high) / 2.0;
            double diff = areaDifference(squares, mid);

            if (diff > 0) {
                low = mid;
            } else {
                high = mid;
            }
        }

        return low;
    }

    // areaAbove - areaBelow
    private double areaDifference(int[][] squares, double yLine) {
        double above = 0.0;
        double below = 0.0;

        for (int[] sq : squares) {
            double y = sq[1];
            double side = sq[2];
            double top = y + side;
            double area = side * side;

            if (top <= yLine) {
                // Entire square below
                below += area;
            } else if (y >= yLine) {
                // Entire square above
                above += area;
            } else {
                // Square is cut by the line
                double aboveHeight = top - yLine;
                double belowHeight = yLine - y;

                above += aboveHeight * side;
                below += belowHeight * side;
            }
        }

        return above - below;
    }
}
