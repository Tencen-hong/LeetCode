class Solution:
    '''
    先忽略符号，以绝对值形式求a/b的结果：a/b的结果是结果的整数部分，如果余数r = a % b不等于0，说明还有小数部分
    用map标记余数r应该在result的哪个位置，如果map[r]不为0说明出现过，那么就在m[r]（出现的位置）的前面添加一个(，在result结尾添加一个)，表示这部分会循环
    1.如果除数等于0，直接返回0，为了避免出现返回-0的情况～
    2.如果numerator,denominator他们一正一负，结果是负数，所以要在result的第一位添加一个“-”。
    3.如果一开始的r不等于0，说明有小数部分，则在计算小数部分之前添加一个”.”
    '''

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        result = []
        if numerator*denominator < 0:
            result.append('-')
        a, b = abs(numerator), abs(denominator)
        result += str(a//b)
        r = a % b
        if r != 0:
            result.append('.')
        m = {}
        while r != 0:
            if r in m:
                result.insert(m[r], '(')
                result.append(')')
                break
            m[r] = len(result)
            r = r*10
            result.append(str(r//b))
            r = r % b
        return ''.join(result)
