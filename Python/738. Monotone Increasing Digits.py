class Solution:
    '''
    从高位向低位遍历整数N的各位数，找到第一个违反单调不减的数的下标x
    将x位后的所有数替换为0，记得到的新数为M，则M - 1即为答案
    '''

    def monotoneIncreasingDigits(self, N: int) -> int:
        sn = str(N)
        size = len(sn)
        flag = False
        for x in range(size - 1):
            if sn[x] > sn[x + 1]:
                flag = True
                break
        if not flag:
            return N
        while x > 0 and sn[x - 1] == sn[x]:
            x -= 1
        y = len(sn) - x - 1
        return (N // (10 ** y)) * (10 ** y) - 1
