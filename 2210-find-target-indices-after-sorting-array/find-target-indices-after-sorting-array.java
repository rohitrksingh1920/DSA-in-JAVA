class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int number = 0;
        int tcount = 0;

        for(int ele : nums) {
            if(ele == target) {
                tcount++;
            }
            else if(ele < target) {
                number++;
            }
        }

        List<Integer> ans = new ArrayList<>();

        while(tcount > 0) {
            ans.add(number);
            number++;
            tcount--;
        }

        return ans;
    }
}