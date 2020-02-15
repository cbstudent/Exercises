# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        prev = root
        cur = root
        
        while cur:
            prev = cur
            if val >= cur.val:
                cur = cur.right
            else:
                cur = cur.left
                
                
        nn = TreeNode(val)
        if val >= prev.val:
            prev.right = nn
        else:
            prev.left = nn

        return root
