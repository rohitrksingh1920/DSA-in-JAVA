// class Solution {
//     public int minimumDifference(int[] nums, int k) {

//         if(k == 1) {
//             return 0;
//         }

//         Arrays.sort(nums);
//         int minDiff = Integer.MAX_VALUE;

//         for(int i = 0; i <= nums.length + k - 2; i++) {
//             for(int j = i; j <= nums.length - 1; j++) {
//                 if(j - i + 1 == k) {
//                     minDiff = Math.min(minDiff, nums[j] - nums[i]);
//                     break;
//                 }
//             }
//         }
//         return minDiff;
//     }
// }

class Solution {
    public int minimumDifference(int[] nums, int k) {
        if (k == 1) {
            return 0;
        }

        Arrays.sort(nums);
        int minDiff = Integer.MAX_VALUE;

        for (int i = 0; i + k - 1 <= nums.length - 1; i++) {
            minDiff = Math.min(minDiff, nums[i + k - 1] - nums[i]);
        }

        return minDiff;
    }
}
