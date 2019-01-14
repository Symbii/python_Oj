def searchBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    # 如果树不存在返回空
    if root == None:
        return None

    # 如果相等返回节点
    if root.val == val:
        return root

    # 访问左右子树
    rightroot = self.searchBST(root.right, val)
    leftroot = self.searchBST(root.left, val)

    # 哪个子树不为空返回哪个
    if rightroot:
        return rightroot
    elif leftroot:
        return leftroot
    else:
        return None
