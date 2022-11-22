class solution:
    def haspathsum(self, root: treenode, targetsum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]  # [(当前节点，路径数值), ...]

        while stack:
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetsum:
                return True

            if cur_node.right:
                stack.append((cur_node.right, path_sum + cur_node.right.val))

            if cur_node.left:
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return False
