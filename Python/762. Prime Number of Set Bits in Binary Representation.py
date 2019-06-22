class Solution:
    '''
    1.创建一个100以内的素数表
    2.将L-R之间的数转成2进制('1'的位数不会超过100)
    3.统计'1'位数是素数的数量
    '''

    def countPrimeSetBits(self, L: int, R: int) -> int:
        def isPrime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        def countPrimeSet(N):
            s = [1]*(N+1)
            for i in range(N+1):
                if s[i] == 0:
                    continue
                if isPrime(i):
                    s[i] = 1
                    for j in range(2*i, N+1, i):
                        s[j] = 0
                else:
                    s[i] = 0
            return [i for i in range(len(s)) if s[i] == 1]

        prime_set = countPrimeSet(100)
        ans = 0
        for i in range(L, R+1):
            binary_i = bin(i)
            binary_i_bits = binary_i.count('1')
            if binary_i_bits in prime_set:
                ans += 1
        return ans
