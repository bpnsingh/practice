class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        ans= []
        for i in range(N):
            row_sum = 0
            for j in range(M):
                row_sum += A[i][j]
            ans.append(row_sum)
        return row_sum

A=[[1,2,3,4],
   [5,6,7,8],
   [9,2,3,4]]
scaler = Solution()
print (scaler.solve(A))