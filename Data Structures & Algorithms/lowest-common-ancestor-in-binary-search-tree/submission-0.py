# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        node = root 
        if p.val > q.val:
            p,q = q,p

         
        if node.val >= p.val and node.val <= q.val:
            return node
        
        elif node.val < p.val:
            return self.lowestCommonAncestor(node.right,p,q)
        else:
            return self.lowestCommonAncestor(node.left,p,q)
        