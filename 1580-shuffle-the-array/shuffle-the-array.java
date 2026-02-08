class Solution {
    public int[] shuffle(int[] nums, int n) {

        int start = 0;
        int mid = n;

        int[] arr = new int[nums.length];

        for(int i = 0; i <= nums.length-1; i++) {
            if (i%2 == 0) {
                arr[i] = nums[start];
                start ++;
            }
            else {
                arr[i] = nums[mid];
                mid ++;  
            }
        }
        return arr;
    }
}

