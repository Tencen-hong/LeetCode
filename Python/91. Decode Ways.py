class Solution:

    '''
    code[i]代表前i个字符可解码的数量
    很明显可知code[i]的值与code[i-1]、code[i-2]都有关，当出现诸如s[i-1]='2'且s[i-2]='1'的情况时，code[i]=code[i-1]+code[i-2]，否则code[i]=code[i-1]。
    当s[i-1]='0'时code[i-1]=0的情况，因为s[i-1]='0'时它本身是不能进行解码的，因此code[i-1]必须设为0。
    '''

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        prefix = [0]*(n+1)
        prefix[0] = 1

        for i in range(1, n+1):
            if s[i-1] == '0':
                prefix[i-1] = 0
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'):
                prefix[i] = prefix[i-1]+prefix[i-2]
            else:
                prefix[i] = prefix[i-1]

        return prefix[-1]
