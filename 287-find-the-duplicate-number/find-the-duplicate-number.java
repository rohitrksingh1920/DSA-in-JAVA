class Solution {
    public int findDuplicate(int[] nums) {
        int ans = 0;

        for(int i = 0; i <= nums.length-1; i++) {
            int ele =  nums[i];
            ele = Math.abs(ele);

            if(nums[ele] > 0) {
                nums[ele] = -nums[ele];
            }
            else{
                ans = ele;
                break;
            }
        }
        for(int i = 0; i <= nums.length-1; i++) {
            nums[i] = Math.abs(nums[i]);
        }
        return ans;
    }
}