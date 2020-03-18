class Solution:
    '''
    将表达式拆成 a op b 的形式,  再将a的所有可能结果与b的所有可能结果做运算
    '''

    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []
        for i in range(len(input)):
            c = input[i]
            if c in "*+-":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for r1 in res1:
                    for r2 in res2:
                        if c == '+':
                            result.append(r1 + r2)
                        elif c == '-':
                            result.append(r1 - r2)
                        elif c == '*':
                            result.append(r1 * r2)

        if not result:
            result.append(int(input))
        return result
