# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp != None:
            count += 1
            temp = temp.next

        middle = count//2
        temp = head

        for i in range(middle):
            temp = temp.next
        
        return temp
