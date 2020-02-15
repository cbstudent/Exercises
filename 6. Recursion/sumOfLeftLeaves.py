# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        sum = 0
        
        q = [root]
        qd = [False]
        
        
        while len(q):
            
            node = q.pop(0)
            isLeft = qd.pop(0)
            
            if not node:
                continue
                
            if not node.left and not node.right and isLeft:
                sum += node.val
            
            q.append(node.left)
            qd.append(True)
            q.append(node.right)
            qd.append(False)
        
        return sum
            
        
        
