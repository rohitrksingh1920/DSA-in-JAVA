class Solution {
    public int maxPower(String s) {
        int max = 1;
        int count = 1;

        for(int i = 1; i <= s.length()-1; i++) {
            int pre = s.charAt(i-1);
            int curr = s.charAt(i);

            if(pre == curr) {
                count++;
            }
            else {
                max = Math.max(max, count);
                count = 1;
            }
        }

        max = Math.max(max, count);
        return max;
    }
}