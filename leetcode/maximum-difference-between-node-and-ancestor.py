# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def maxAncestorDiff(self, root: Optional[TreeNode], miN=float('inf'), maX=float('-inf')) -> int:
        if not root:
            return maX-miN

        miN = min(miN, root.val)
        maX = max(maX, root.val)

        left = self.maxAncestorDiff(root.left, miN,maX)
        right = self.maxAncestorDiff(root.right, miN,maX)

        return max(left,right)