class Solution {
    public int longestConsecutive(int[] nums) {

        HashMap<Integer, Boolean> hm = new HashMap<>();

        // Step 1: Put all numbers in map
        for (int i = 0; i < nums.length; i++) {
            hm.put(nums[i], false);
        }

        // Step 2: Mark starting points of sequences
        for (int key : hm.keySet()) {
            if (hm.containsKey(key - 1) == false) {
                hm.put(key, true); // this key is the start of a sequence
            }
        }

        // Step 3: Find longest sequence
        int max = 0;
        for (int key : hm.keySet()) {
            int k = 1;
            if(hm.get(key) == true) {
                while (hm.containsKey(key + k)) {
                    k++;
                }
            }
            max = Math.max(max, k);
        }
        return max;
    }
}