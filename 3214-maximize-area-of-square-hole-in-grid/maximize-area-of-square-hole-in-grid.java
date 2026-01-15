class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int maxHGap = getMaxGap(hBars);
        int maxVGap = getMaxGap(vBars);

        int side = Math.min(maxHGap, maxVGap);
        return side * side;
    }

    private int getMaxGap(int[] bars) {
        if (bars.length == 0) return 1;

        Arrays.sort(bars);

        int maxGap = 1;
        int curr = 1;

        for (int i = 1; i < bars.length; i++) {
            if (bars[i] == bars[i - 1] + 1) {
                curr++;
            } else {
                curr = 1;
            }
            maxGap = Math.max(maxGap, curr);
        }

        return maxGap + 1;
    }
}
