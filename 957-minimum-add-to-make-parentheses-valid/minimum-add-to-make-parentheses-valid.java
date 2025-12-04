class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> st = new Stack<>();

        int count = 0;

        for(int i = 0; i <= s.length()-1; i++) {
            char ch = s.charAt(i);

            if(ch == '(') {
                st.push(ch);
            }
            else if(st.size() > 0 && st.peek() == '(') {    //when we have ')'
                st.pop();
            }
            else {
                count++;
            }
        }
        return count + st.size();
    }
}