class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    :type root: TreeNode
    :rtype: bool
    """
    def isUnivalTree(self, root):
        def dfs(node):
            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)

        return dfs(root)