class Solution {
    public int maxAscendingSum(int[] nums) {
        int sum = nums[0];
        int Currsum = nums[0];

        for(int i = 1; i < nums.length; i++) {
            if(nums[i-1] < nums[i]) {
                Currsum += nums[i]; 
            }
            else {
                sum = Math.max(sum, Currsum);
                Currsum = nums[i]; 
            }
        }
        sum = Math.max(sum, Currsum);
        return sum;
    }
}