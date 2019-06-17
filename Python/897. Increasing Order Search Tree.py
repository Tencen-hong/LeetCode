# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
        1.记录中序遍历的结果
        2.将1中每个节点左孩子设None，右孩子指向下一个节点
    '''

    def increasingBST(self, root: TreeNode) -> TreeNode:
        inlist = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            inlist.append(root)
            inOrder(root.right)
        inOrder(root)

        for i in range(len(inlist)-1):
            inlist[i].left = None
            inlist[i].right = inlist[i+1]

        inlist[-1].right = inlist[-1].left = None

        return inlist[0]
