class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self,i,j,A,N,dp):
        if i == N-1:
            return A[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        down = A[i][j] + self.solve(i+1,j,A,N,dp)
        diagonal = A[i][j] + self.solve(i+1,j+1,A,N,dp)
        dp[i][j] = min(down,diagonal)
        return dp[i][j]
    def minimumTotal(self, A):
        N = len(A)
        M = len(A[-1])
        dp = [[-1]*(M+1) for i in range(N+1)]
        return  self.solve(0,0,A,N,dp)

scaler = Solution()
A= [     [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
print(scaler.minimumTotal(A))


