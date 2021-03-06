# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        if root:
            tmp = root.right
            root.right = root.left
            root.left = tmp
        if root.left: self.invertTree(root.left)
        if root.right: self.invertTree(root.right)
        return root
