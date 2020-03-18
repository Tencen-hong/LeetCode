class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        flag = 0
        for i in range(1, len(A)):  # 递增
            if A[i-1] > A[i]:
                flag = 1
                break

        if flag == 1:
            for i in range(1, len(A)):  # 递减
                if A[i-1] < A[i]:
                    flag = 2
                    break
        if flag == 2:
            return False
        else:
            return True
