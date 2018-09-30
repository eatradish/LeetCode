# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.symmetric(root.left, root.right)
    def symmetric(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        return left.val == right.val and self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)


