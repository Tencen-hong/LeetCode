class Solution:
    '''
    用一个栈，从字符串的左侧向右依次进栈，如果满足栈的后三位是数字，#，#的模式时，说明可以构成合法的叶子节点，把这个叶子节点换成#号，代表空节点，然后继续遍历。最后应该只剩下一个#，那么就是一个合法的二叉树。

    如：”9,3,4,#,#,1,#,#,2,#,6,#,#” 遇到x # #的时候，就把它变为 #

    模拟一遍过程：

    9,3,4,#,# => 9,3,# 继续读
    9,3,#,1,#,# => 9,3,#,# => 9,# 继续读
    9,#2,#,6,#,# => 9,#,2,#,# => 9,#,# => #

    '''

    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        st = []
        for node in preorder:
            st.append(node)
            while len(st) >= 3 and st[-1] == '#' and st[-2] == '#' and st[-3] != '#':
                st.pop()
                st.pop()
                st.pop()
                st.append('#')
        return len(st) == 1 and st[0] == '#'
