class Solution {
    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        long left = 1;
        long right = (long)1e18;
        long ans = right;

        while (left <= right) {
            long mid = left + (right - left) / 2;

            if (canReduce(mid, mountainHeight, workerTimes)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return ans;
    }

    private boolean canReduce(long time, int mountainHeight, int[] workerTimes) {
        long total = 0;

        for (int w : workerTimes) {
            long h = (long)((Math.sqrt(1 + 8.0 * time / w) - 1) / 2);
            total += h;

            if (total >= mountainHeight)
                return true;
        }

        return total >= mountainHeight;
    }
}