class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Idea: Each time check current node's left node.
              If current node don't have one, skip it.
        """
        stack = []
        if root:
            stack.append(root)
        res = 0

        while stack:
            # 每次都把当前节点的左节点加进去.
            cur_node = stack.pop()
            if cur_node.left and not cur_node.left.left and not cur_node.left.right:
                res += cur_node.left.val

            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

        return res