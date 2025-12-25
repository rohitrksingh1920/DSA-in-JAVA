class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        long sum = 0;
        int n = happiness.length;

        for (int i = 0; i < k; i++) {
            int value = happiness[n - 1 - i] - i;
            if (value > 0) {
                sum += value;
            }
        }
        return sum;
    }
}
