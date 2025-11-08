class Solution {
    public int maxSubArray(int[] nums) {
        int currsum = nums[0];
        int maxsum = nums[0];

        for(int i = 1; i <= nums.length-1; i++) {
            if(currsum + nums[i] > nums[i]) {
                currsum += nums[i];
            }
            else {
                currsum = nums[i];
            }
            maxsum = Math.max(maxsum, currsum);
        }
        return maxsum;
    }
}