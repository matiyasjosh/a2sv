# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(nodeLeft, nodeRight):
            if nodeLeft is None and nodeRight is None:
                return True
            if nodeLeft is None or nodeRight is None or nodeLeft.val != nodeRight.val:
                return False
            return isMirror(nodeLeft.left, nodeRight.right) and isMirror(nodeLeft.right, nodeRight.left)


        if not root:
            return True

        return isMirror(root.left, root.right)