# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        end = head

        while end.next:
            end = end.next
            length += 1

        end.next = head

        k = k % length

        stepToNewEnd = length - k - 1

        newEnd = head
        for i in range(stepToNewEnd):
            newEnd = newEnd.next

        newHead = newEnd.next
        newEnd.next = None

        return newHead