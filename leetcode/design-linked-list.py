class Node: 
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.head = None        
        self.length = 0
    def get(self, index: int) -> int:
        if index<0 or index>=self.length:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr is None:
                return -1
        return curr.val
    def addAtHead(self, val: int) -> None:
        newNode = Node(val, self.head)
        self.head = newNode
        self.length+=1
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        self.length+=1
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.length:
            return
        if index==0:
            self.addAtHead(val)
        elif index==self.length:
            self.addAtTail(val)
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            newNode = Node(val, curr.next)
            curr.next = newNode
            self.length+=1
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.length:
            return
        if index==0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index-1):
                curr=curr.next
            curr.next = curr.next.next
        self.length-=1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)