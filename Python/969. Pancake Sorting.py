class Solution:
    '''
        将原列表看成前半部分未排序后半部分已排序
        每轮循环从未排序的列表中选出最大的数的下标
        翻转此下标之前的列表，此时最大数移到了表头
        翻转整个未排序列表，此时最大数移到了以排序的表头
        每轮循环都能确定一个最大数

    '''

    def pancakeSort(self, A: List[int]) -> List[int]:
        result = []
        for i in range(len(A), 1, -1):
            max_value = max(A[:i])
            max_index = A.index(max_value)
            result.append(max_index+1)
            A[:max_index+1] = A[max_index::-1]
            result.append(i)
            A[:i] = A[i-1::-1]
        print(A)
        return result
