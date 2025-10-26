class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] right = new int[nums.length];
        int[] ans = new int[nums.length];

        int product = 1;

        for(int i = nums.length-1; i >= 0; i--) {
            product *= nums[i];
            right[i] = product; 
        }
        int left = 1;

        for(int i = 0; i < nums.length-1; i++) {
            int val = left * right[i+1];

            ans[i] = val;
            left *= nums[i];
        }
        ans[nums.length-1] = left;

        return ans;
    }
}