# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x=0):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next=  nextNode.next 