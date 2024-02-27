class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
         self.dummy=Node()
    def get(self, index: int) -> int:
        temp = self.dummy
        for _ in range(index+1):
            temp=temp.next
            if temp is None: return -1

        return temp.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val) 
        newNode.next = self.dummy.next
        self.dummy.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        temp = self.dummy
        while temp.next:
            temp=temp.next
        temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        prev = self.dummy
        for _ in range(index):
            prev=prev.next
            if not prev: return
        newNode.next=prev.next
        prev.next=newNode

    def deleteAtIndex(self, index: int) -> None:
        prev = self.dummy
        for _ in range(index):
            prev=prev.next
            if not prev.next: return
        prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)