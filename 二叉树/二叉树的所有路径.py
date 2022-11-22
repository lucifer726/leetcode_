# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        path = ''
        result = []
        if not root: return result
        self.traversal(root, path, result)
        return result

    def traversal(self, cur: TreeNode, path: str, result):
        path += str(cur.val)
        # 若当前节点为leave，直接输出
        if not cur.left and not cur.right:
            result.append(path)

        if cur.left:
            # + '->' 是隐藏回溯
            self.traversal(cur.left, path + '->', result)

        if cur.right:
            self.traversal(cur.right, path + '->', result)


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6)))
    tree = Solution()
    print(tree.binaryTreePaths(root))
