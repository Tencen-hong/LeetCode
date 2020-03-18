class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """

        left, top = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                left = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[i])-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if left:
                matrix[i][0] = 0

#         left,top=False,False
#         for i in range(len(matrix)):
#             if matrix[i][0]==0:
#                 left=True
#         for j in range(len(matrix[0])):
#             if matrix[0][j]==0:
#                 top=True
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j]==0:
#                     matrix[i][0]=0
#                     matrix[0][j]=0

#         for i in range(1,len(matrix)):
#             if matrix[i][0]==0:
#                 matrix[i] = [0]*len(matrix[i])
#         for j in range(1,len(matrix[0])):
#             if matrix[0][j]==0:
#                 for i in range(1,len(matrix)):
#                     matrix[i][j]=0
#         if left:
#             for i in range(len(matrix)):
#                 matrix[i][0]=0
#         if top:
#             for j in range(len(matrix[0])):
#                 matrix[0][j]=0
