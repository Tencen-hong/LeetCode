# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    '''
    采用前序遍历. 

    序列化，即将二叉树转成字符串。因为二叉树中包含null节点。需要采用一个特殊字符标记，因为这里的二叉树的值都是数字，所以可以采用非数字作为标记，如采用X。每个节点间用,分割。然后就是按照前序遍历的方法，输入二叉树成字符串。

    反序列化，即将刚才生成的字符串转换成二叉树。首先，将字符串按照,split成字符串数组的形式，该数组中每一个元素即为一个二叉树的节点。这里本来可以很简单的用一个全局变量记录，当前遍历的数组index，但是因为题目中要求采用stateless的方式，所以必须换种方式。可以采用list的方式，将已经遍历的节点删除，剩下的就是当该字符串不是X时，按照前序遍历的方式重建二叉树。
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        sl = []

        def buildString(root, sl):
            if root == None:
                sl.append('X')
            else:
                sl.append(str(root.val))
                buildString(root.left, sl)
                buildString(root.right, sl)

        buildString(root, sl)

        return ','.join(sl)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(',')

        def buildTree(data):
            val = data.pop(0)
            if val == 'X':
                return None
            else:
                node = TreeNode(val)
                node.left = buildTree(data)
                node.right = buildTree(data)
                return node

        return buildTree(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
