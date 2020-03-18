class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        "if x < 0 return false"
        if (x < 0):
            return False

        "convert x to string"
        x = str(x)

        "whether x == reverse of x"
        return x == x[::-1]
