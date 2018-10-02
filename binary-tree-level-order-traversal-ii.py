class Solution:
    def _levelOrderBottom(self, level, result, node):
        if node:
            if level > len(result):
                result.insert(0, [])

            result[-level].append(node.val)
            self._levelOrderBottom(level + 1, result, node.left)
            self._levelOrderBottom(level + 1, result, node.right)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level, result = 1, []
        self._levelOrderBottom(level, result, root)
        return result
