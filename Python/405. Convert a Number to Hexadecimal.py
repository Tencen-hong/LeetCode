class Solution:
    def toHex(self, num: int) -> str:
        map = ['0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        if num == 0:
            return "0"
        ret = ""
        for i in range(8):
            ret = map[num & 0x0f] + ret
            num >>= 4
        return ret.lstrip('0')
