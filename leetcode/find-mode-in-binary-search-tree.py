# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d=defaultdict(int)
        def findIt(node):
            if not node: return
            
            d[node.val]+=1
            findIt(node.left)
            findIt(node.right)
        
        findIt(root)
        m = max(d.values())
        return [keys for keys, values in d.items() if values==m]