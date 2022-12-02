class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None  # 节点为空，返回
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # 当前节点的左子树为空，返回当前的右子树
            if not root.left: return root.right
            # 当前节点的右子树为空，返回当前的左子树
            if not root.right: return root.left
            # 左右子树都不为空，找到右孩子的最左节点 记为p
            node = root.right
            while node.left:
                node = node.left
            # 将当前节点的左子树挂在p的左孩子上
            node.left = root.left
            # 当前节点的右子树替换掉当前节点，完成当前节点的删除
            root = root.right
        return root
