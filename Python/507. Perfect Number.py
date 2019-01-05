class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 3:
            return False

        factors = set()
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                factors.add(i)
                factors.add(num//i)

        factors = list(factors)
        if sum(factors) == num-1:
            return True
        return False
