# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def rangeS(node):
            if not node: return None
            rangeS(node.left)
            nonlocal res
            if node.val >= low and node.val <= high:
                res += node.val
            if node.val > high:
                return res
            rangeS(node.right) 

            return res

        return rangeS(root)