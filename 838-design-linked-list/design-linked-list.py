# class Node:
#     def __init__(self, val=0):
#         self.val = val
#         self.prev = None
#         self.next = None

# class MyLinkedList:

#     def __init__(self):
#         self.head = Node(0)   # dummy head
#         self.tail = Node(0)   # dummy tail
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.size = 0
        

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
        
#         curr = self.head.next
#         for _ in range(index):
#             curr = curr.next
        
#         return curr.val
        

#     def addAtHead(self, val: int) -> None:
#         self._add_between(val, self.head, self.head.next)
        

#     def addAtTail(self, val: int) -> None:
#         self._add_between(val, self.tail.prev, self.tail)
        

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return
        
#         curr = self.head.next
#         for _ in range(index):
#             curr = curr.next
        
#         self._delete_node(curr)

#     def _add_between(self, val, prev_node, next_node):
#         new_node = Node(val)
#         new_node.prev = prev_node
#         new_node.next = next_node
        
#         prev_node.next = new_node
#         next_node.prev = new_node
        
#         self.size += 1
        
        

#     # def deleteAtIndex(self, index: int) -> None:

#      # Helper to delete node
#     def _delete_node(self, node):
#         prev_node = node.prev
#         next_node = node.next
        
#         prev_node.next = next_node
#         next_node.prev = prev_node
        
#         self.size -= 1








class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)   # dummy head
        self.tail = Node(0)   # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        self._add_between(val, self.head, self.head.next)

    def addAtTail(self, val: int) -> None:
        self._add_between(val, self.tail.prev, self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        self._add_between(val, curr, curr.next)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        self._delete_node(curr)

    # Helper to add node
    def _add_between(self, val, prev_node, next_node):
        new_node = Node(val)
        new_node.prev = prev_node
        new_node.next = next_node
        
        prev_node.next = new_node
        next_node.prev = new_node
        
        self.size += 1

    # Helper to delete node
    def _delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.size -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)