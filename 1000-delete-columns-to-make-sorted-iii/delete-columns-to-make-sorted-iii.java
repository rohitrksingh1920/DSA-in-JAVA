class Solution {
    public int minDeletionSize(String[] strs) {
        int cols = strs[0].length();
        int rows = strs.length;

        int[] dp = new int[cols];
        int maxLen = 1;

        for (int i = 0; i < cols; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (isValid(strs, j, i)) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            
            maxLen = Math.max(maxLen, dp[i]);
        }

        return cols - maxLen;
    }

    private boolean isValid(String[] strs, int c1, int c2) {
        for (String s : strs) {
            if (s.charAt(c1) > s.charAt(c2)) {
                return false;
            }
        }
        return true;
    }
}
