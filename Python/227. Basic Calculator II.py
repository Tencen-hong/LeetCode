class Solution:
    '''
    利用堆栈实现基本运算，对给定的字符串进行轮训，如果是数字且操作符是+或者-号，则将该数字压入到堆栈中，如果是操作符是*或者/号，则将栈顶元素取出之后与当前数字进行运算，将运算结果保存到堆栈中。最后堆栈中所保存的数字之间均为+运算关系，则只需要将堆栈中的数字进行累加即可获得运算结果值。

    '''

    def calculate(self, s: str) -> int:
        s += '+0'
        stack, num, preOp = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+int(s[i])
            elif not s[i].isspace():
                if preOp == '+':
                    stack.append(num)
                elif preOp == '-':
                    stack.append(-num)
                elif preOp == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                preOp, num = s[i], 0
        return sum(stack)
