class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;

        for(int ele : nums) {
            sum += ele;
        }
        int r_sum = sum;
         int l_sum = 0;

         for(int i = 0; i <= nums.length-1; i++) {
            r_sum -= nums[i];

            if(r_sum == l_sum) {
                return i;
            }
            else {
                l_sum += nums[i];
            }
        }
        return -1;
    }
}