# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slowNode = head
        fastNode = head

        while fastNode != None and fastNode.next != None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next

        prevNode = None
        currNode = slowNode

        while currNode != None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        leftNode = head
        rightNode = prevNode

        while rightNode != None:
            if leftNode.val != rightNode.val:
                return False

            leftNode = leftNode.next
            rightNode = rightNode.next

        return True
        
