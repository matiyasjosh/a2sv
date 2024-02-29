# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less_curr = less_head
        greater_curr = greater_head

        curr = head
        while curr:
            if curr.val < x:
                less_curr.next = curr
                less_curr = less_curr.next
            else:
                greater_curr.next = curr
                greater_curr = greater_curr.next
            curr = curr.next

        greater_curr.next = None  # Set the next of greater_curr to None to avoid cycles
        less_curr.next = greater_head.next  # Combine the two partitions

        return less_head.next