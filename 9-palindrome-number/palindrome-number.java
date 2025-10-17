class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) {
            return false;
        }
        int num = x;
        int revNum = 0;
        while(num>0) {
            int last_d = num%10;
            revNum = revNum*10 + last_d;
            num = num/10;
        }
        if(revNum == x) {
            return true;
        }
        else {
            return false;
        }
    }
}