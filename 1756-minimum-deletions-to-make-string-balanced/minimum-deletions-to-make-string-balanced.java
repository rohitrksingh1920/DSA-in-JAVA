class Solution {
    public int minimumDeletions(String s) {
        int n = s.length();
        int bcount = 0;
        int ans = 0;
        
        for(char ch : s.toCharArray()) {
            if(ch=='a') {
                ans = Math.min(bcount, 1+ans);
            }
            else bcount++;
        }
        return ans;
    }
}