class Solution {
    public int minPartitions(String n) {
        int max = 0;

        for(int i = 0; i <= n.length()-1; i++) {
            int currChVal = n.charAt(i)-'0';

            max = Math.max(max, currChVal);
        }

        return max;
    }
}