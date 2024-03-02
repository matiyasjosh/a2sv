# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def visit(node,ans):
            if node:
                ans += str(node.val)
            if not node.right and not node.left:
                res.append(ans)
            if node.left:
                visit(node.left,ans)
            if node.right:
                visit(node.right,ans)
        visit(root,"")

        return sum(map(int, res))
