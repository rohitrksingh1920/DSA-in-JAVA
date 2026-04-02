# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return
        
        stack = []
        curr = head
        
        while curr:
            stack.append(curr)
            curr = curr.next
        
        newHead = stack.pop()
        curr = newHead
        
        while stack:
            node = stack.pop()
            curr.next = node
            curr = curr.next
        
        curr.next = None
        
        return newHead