class Solution {
    public int fib(int n) {
        // using itrative approach

        if(n <= 1) {
            return n;
        }
        
        int first_term = 0;
        int second_term = 1;

        for(int i = 1; i<= n; i++) {
            int third_term = first_term + second_term;

            first_term = second_term;
            second_term = third_term;
        }
        return first_term;
    }
}