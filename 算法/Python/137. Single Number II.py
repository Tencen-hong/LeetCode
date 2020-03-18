class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        A = {}

        for num in nums:
            if num not in A.keys():
                A[num] = 1
            elif A[num] == 1:
                A[num] = 2
            elif A[num] == 2:
                A.pop(num)

        res = list(A.keys())
        return res[0]
