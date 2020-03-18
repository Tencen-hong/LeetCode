
'''
将a-z的个数统计映射到int型的bit上
'''
class Solution:
    def isUnique(self, astr: str) -> bool:
        mask = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if (mask & 1<<move_bit) != 0:
                return False
            else:
                mask |= 1<<move_bit
        return True