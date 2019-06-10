class Solution:
    '''
        根据逆波兰式性质
        遇见数字压入栈中
        遇见运算符连续出2栈2个数，运算后再将结果入栈
    '''

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        for ch in tokens:
            if ch not in op:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(a+b)
                elif ch == '-':
                    stack.append(a-b)
                elif ch == '*':
                    stack.append(a*b)
                elif ch == '/':
                    stack.append(int(a/b))
        return stack[-1]
