
class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    Your Codec object will be instantiated and called as such:
    codec = Codec()
    codec.deserialize(codec.serialize(root))
    """
    def serialize_recursive(self, root, output):
        if not root:
            output.append(None)
        else:
            output.append(root.val)
            self.serialize_recursive(root.left, output)
            self.serialize_recursive(root.right, output)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = []
        self.serialize_recursive(root, output)
        while output and output[-1] is not None:
            output.pop()
        output.reverse()
        output = str(output)
        return output

    def deserialize_recursive(self, data):
        if data:
            x = data.pop()
            if x is not None:
                node = TreeNode(x)
                node.left = self.deserialize_recursive(data)
                node.right = self.deserialize_recursive(data)
                return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        return self.deserialize_recursive(data)
