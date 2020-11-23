# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        left = []
        node = root.left
        while node:
            left.append(node.val)
            if node.left:
                node = node.left
            else: # if we can't find a left node, try going right
                node = node.right
        left = left[:-1] # trim last element because it is a leaf

        right = []
        node = root.right
        while node:
            right.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left            
        right = right[:-1]

        leaves = self.getLeaves(root)
        
        # don't forget to reverse right
        return [root.val] + left + leaves + right[::-1] 

    def getLeaves(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]

        return self.getLeaves(node.left) + self.getLeaves(node.right)
            
