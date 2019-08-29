class Solution:
    '''
    在l起点下，中间点m距离x最近
    '''

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-k
        while l < r:
            m = (l+r)//2
            if abs(arr[m]-x) > abs(arr[m+k]-x):
                l = m + 1
            else:
                r = m

        return arr[l:l+k]
