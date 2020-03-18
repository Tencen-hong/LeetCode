class Solution:
    '''
       1.要使B的difference最小，A中所有元素要向中间趋近
       2.左边界为min(A)+K , 右边界为max(A)-K
         左边界即为min(B) , 右边界即为max(B)
       3.右边界<左边界说明有交叉，B中所有元素能达到同一个值
       3.左边界<右边界说明B中没有重合部分，return max(B)-min(B)
    '''

    def smallestRangeI(self, A: List[int], K: int) -> int:
        right = max(A)-K
        left = min(A)+K
        if right <= left:
            return 0
        else:
            return right-left
