class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        N =len(A)
        ans = []
        ans_size = 2*N - 1
        for i in range(ans_size):
            ans.append([0]*N)
        print (ans)
        for col in range(N):
            start_col = col
            start_row = 0
            while (start_col>=0) and (start_row < N):
                ans[start_row][start_col]=A[start_row][start_col]
                start_col -= 1
                start_row += 1
        print (ans)
        for row in range(1,N):
            start_row = row
            start_col = N-1
            while (start_col >= 0) and (start_row < N):
                ans[start_row][start_col] = A[start_row][start_col]
                start_col -= 1
                start_row += 1
        return ans

scaler = Solution()
A=[[1,2,3],[4,5,6],[7,8,9]]
print(scaler.diagonal(A))