# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case
        if root is None:
            return None

        # If either n1 or n2 matches with root's key, report
        #  the presence by returning root (Note that if a key is
        #  ancestor of other, then the ancestor key becomes LCA
        if root.val == p.val or root.val == q.val:
            return root 

        # Look for vals in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q) 
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both of the above calls return Non-NULL, then one key
        # is present in once subtree and other is present in other,
        # So this node is the LCA
        if left_lca and right_lca:
            return root 

        # Otherwise check if left subtree or right subtree is LCA
        return left_lca if left_lca is not None else right_lca

        
