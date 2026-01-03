class Solution {
    public int numOfWays(int n) {
        long MOD = 1_000_000_007;

        long aba = 6;
        long abc = 6;

        for (int i = 2; i <= n; i++) {
            long newAba = (3 * aba + 2 * abc) % MOD;
            long newAbc = (2 * aba + 2 * abc) % MOD;

            aba = newAba;
            abc = newAbc;
        }

        return (int)((aba + abc) % MOD);
    }
}
