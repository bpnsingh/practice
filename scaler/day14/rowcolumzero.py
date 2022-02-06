class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        row_list = []
        column_list = []
        for i in range(N):
            for j in range(M):
                if A[i][j] == 0:
                    row_list.append(i)
                    column_list.append(j)
        print(row_list)
        print(column_list)
        for i in range(N):
            for j in range(M):
                if i in row_list or j in column_list:
                    A[i][j] = 0

        print (A)

scaler = Solution()
A=[[1,2,3,4],
[5,6,7,0],
[9,2,0,4]]
scaler.solve(A)