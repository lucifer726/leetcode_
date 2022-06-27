# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.alist = []

        def peror(root):
            if root == None:
                self.alist.append('#')
                return
            self.alist.append((str(root.val)))
            peror(root.left)
            peror(root.right)

        peror(root)
        return ','.join(self.alist)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        alen = len(arr)
        if alen == 2: return None
        return self.buildTree(arr)

    def buildTree(self, arr):
        if arr[0] == '#':
            del arr[0]
            return None
        root = TreeNode(int(arr[0]))
        del arr[0]
        root.left = self.buildTree(arr)
        root.right = self.buildTree(arr)
        return root


