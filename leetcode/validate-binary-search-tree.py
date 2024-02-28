# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root: return None
            inorder(root.left)
            self.ans.append(root.val)
            inorder(root.right)

        inorder(root)
        if len(set(self.ans))!=len(self.ans):
            return False
            
        rev = sorted(self.ans)
        return rev==self.ans