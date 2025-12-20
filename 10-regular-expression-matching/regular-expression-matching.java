class Solution {
    public boolean isMatch(String s, String p) {
        int a = p.length();
        int b = s.length();
        boolean[][] ptr = new boolean[b + 1][a + 1];
        ptr[0][0] = true;

        for (int j = 2; j <= a; j++) {
            if (p.charAt(j - 1) == '*') {
                ptr[0][j] = ptr[0][j - 2];
            }
        }

        for (int i = 1; i <= b; i++) {
            for (int j = 1; j <= a; j++) {
                char sc = s.charAt(i - 1);
                char pc = p.charAt(j - 1);

                if (pc == '.' || pc == sc) {
                    ptr[i][j] = ptr[i - 1][j - 1];
                } 
                else if (pc == '*') {
                    ptr[i][j] = ptr[i][j - 2];

                    char prev = p.charAt(j - 2);
                    if (prev == '.' || prev == sc) {
                        ptr[i][j] = ptr[i][j] || ptr[i - 1][j];
                    }
                }
            }
        }
        return ptr[b][a];
    }
}
