class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] ans = new int[nums.length];

        int start = 0;
        int end = nums.length-1;

        int ptr = ans.length-1;

        while(start <= end) {

            int sSq = nums[start] * nums[start];
            int eSq = nums[end] * nums[end];

            if(sSq > eSq) {
                ans[ptr] = sSq;
                start++;
            }
            else {
                ans[ptr] = eSq;
                end--;
            }
            ptr--;
        }
        return ans;
    }
}