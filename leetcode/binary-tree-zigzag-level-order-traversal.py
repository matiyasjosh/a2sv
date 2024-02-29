# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
        self.ans = []
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res=[]
        queue = [root]
        count=0
        while queue:
            curr=[]
            n=len(queue)

            # for reversing we use count
            count+=1
            for _ in range(n):
                node = queue.pop(0)
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(curr if count%2!=0 else curr[::-1])
        return res
        
        
        
        # def zigizaga(root):
        #     if not root: return None
        #     self.count+=1
        #     self.ans.append(root.val)
        #     if self.count%2!=0:
        #         zigizaga(root.right)
        #         zigizaga(root.left)
        #     else:
        #         zigizaga(root.left)
        #         zigizaga(root.right)
        #     return self.ans
        
        # zigizaga(root)
        