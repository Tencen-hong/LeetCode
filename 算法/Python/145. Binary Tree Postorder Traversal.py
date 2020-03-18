# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    先将根节点入栈，再将右节点入栈，最后将左节点入栈
    '''

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans, st = [], [(root, False)]
        while st:
            t, visited = st.pop(-1)
            if t:
                if visited:
                    ans.append(t.val)
                else:
                    st.append((t, True))
                    st.append((t.right, False))
                    st.append((t.left, False))
        return ans
