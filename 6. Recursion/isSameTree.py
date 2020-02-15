# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # Traverse the trees simultaneously
        
        qp = [p]
        qq = [q]
        
        while len(qp) and len(qq):
            nodeq = qq.pop(0)
            nodep = qp.pop(0)
            if not nodeq and not nodep:
                continue
            if nodeq is None or nodep is None:
                return False
            
            if nodeq.val != nodep.val:
                return False
            
                qp.append(nodeq.left)
                qp.append(nodeq.right)
                qq.append(nodeq.left)
                qq.append(nodeq.right)
        
        if len(qp) != len(qq):
            return False
        
        return True
            
