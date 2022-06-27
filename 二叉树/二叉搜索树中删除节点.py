class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return root
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                root = root.right
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root
