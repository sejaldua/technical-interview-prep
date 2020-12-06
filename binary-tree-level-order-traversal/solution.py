# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node, level, d):
            # base case: we have arrived at a child node
            if not node:
                return d
            
            # add node to the proper list / level
            if level in d.keys():
                d[level].append(node.val)
            else:
                d[level] = [node.val]
            
            # recurse on left and right children if possible
            if node.left:
                helper(node.left, level + 1, d)
            if node.right:
                helper(node.right, level + 1, d)
        
            return d
        
        d = helper(root, 0, dict())
        return d.values()
