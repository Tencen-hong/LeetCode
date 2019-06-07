"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    '''
    层次遍历
    然后将同一层的节点连接起来
    '''

    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        level = [root]
        while level:
            size = len(level)
            node_pre = None
            for i in range(size):
                node = level.pop(0)
                if node_pre:
                    node_pre.next = node
                node_pre = node
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return root
