/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> st = new Stack<>();

        ListNode ptr = head;

        while(ptr != null) {
            st.push(ptr.val);
            ptr = ptr.next;
        }

        ListNode ptr2 = head;

        while(ptr2 != null) {
            int val1 = ptr2.val;
            int val2 = st.pop();

            if(val1 != val2) {
                return false;
            }
            else {
                ptr2 = ptr2.next;
            }
        }
        return true;
    }
}