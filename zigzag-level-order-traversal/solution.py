# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: TreeNode, level: int, d: dict) -> List[List[int]]:
        if not node:
            return d
        
        if level in d.keys():
            d[level].append(node.val)
        else:
            d[level] = [node.val]
        
        if node.left:
            self.helper(node.left, level + 1, d)
        if node.right:
            self.helper(node.right, level + 1, d)
        
        return d
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        d = self.helper(root, 0, dict())
        res = []
        for i, key in enumerate(d.keys()):
            if i % 2 == 0:
                res.append(d[key])
            else:
                res.append(reversed(d[key]))
        return res
        
    
       
        
