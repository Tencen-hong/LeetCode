class Solution:
    '''
    1.将N转成2进制
    2.在N中查找相邻的2个'1'，并记录最大的距离
    '''

    def binaryGap(self, N: int) -> int:
        binary = bin(N)
        if binary.count('1') < 2:
            return 0
        result = 0
        start_pos = binary.find('1')
        end_pos = binary.find('1', start_pos,)
        while end_pos != -1:
            result = max(result, end_pos-start_pos)
            start_pos = end_pos
            end_pos = binary.find('1', end_pos+1,)
        return result
