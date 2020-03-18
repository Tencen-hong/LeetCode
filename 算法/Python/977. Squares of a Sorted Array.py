class Solution:
    '''
        1.找到绝对值最小的值的下标
        2.分别在其左右添加平方更小的值
    '''

    def sortedSquares(self, A: List[int]) -> List[int]:
        minn = min([abs(x) for x in A])
        if minn in A:
            minIndex = A.index(minn)
        else:
            minIndex = A.index(-minn)
        i, j = minIndex-1, minIndex+1
        res = [math.pow(A[minIndex], 2)]
        while i >= 0 and j < len(A):
            a = math.pow(A[i], 2)
            b = math.pow(A[j], 2)
            if a < b:
                res.append(a)
                i -= 1
            else:
                res.append(b)
                j += 1
        while i >= 0:
            a = math.pow(A[i], 2)
            res.append(a)
            i -= 1
        while j < len(A):
            b = math.pow(A[j], 2)
            res.append(b)
            j += 1
        return [int(x) for x in res]
