class Solution {
    public int minDeletionSize(String[] strs) {
        boolean[] sorted = new boolean[strs.length - 1];
        int deletions = 0;

        for (int col = 0; col < strs[0].length(); col++) {
            boolean needDelete = false;

            for (int i = 0; i < strs.length - 1; i++) {
                if (!sorted[i] && strs[i].charAt(col) > strs[i + 1].charAt(col)) {
                    needDelete = true;
                    break;
                }
            }

            if (needDelete) {
                deletions++;
            } else {
                for (int i = 0; i < strs.length - 1; i++) {
                    if (!sorted[i] && strs[i].charAt(col) < strs[i + 1].charAt(col)) {
                        sorted[i] = true;
                    }
                }
            }
        }
        return deletions;
    }
}
