class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];

        for (int i = 0; i <= n-1; i++) {
            int x = nums.get(i);

            if (x == 0) {
                ans[i] = -1;
                continue;
            }

            int lowestBit = (x + 1) & -(x + 1);
            int can = x - (lowestBit >> 1);

            if ((can | (can + 1)) == x) {
                ans[i] = can;
            }
            else {
                ans[i] = -1;
            }
        }

        return ans;
    }
}
