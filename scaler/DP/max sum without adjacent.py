'''
Find the maximum possible without adjacent
A = [2,7,9,3,1] ans = 12 (2,9,1)
A = [1,1,100,2,1,101] = 202(1,100,101)
C = [1,1,100,1000,3,101] = 202(1,100,101)
'''
class Solution:
    def solve_dp(self,A):
        N = len(A)
        if N == 1:
            return A[0]
        if N ==2 :
            return max(A)
        dp = []
        for i in range(N):
            if i<=1:
                dp.append(A[i])
            else:
                dp.append(0)
        for i in range(2,N):
            dp[i] = max(A[i]+dp[i-2],dp[i-1])
        return dp[-1]
    def solve(self,A):

        N = len(A)
        dp = [-1] * (N + 1)
        def max_sum(index,A):
            if index >= N:
                return 0
            if dp[index] != -1:
                return dp[index]
            else:
                dp[index] = max(A[index]+max_sum(index+2,A),max_sum(index+1,A))
                return dp[index]
        ans = max_sum(0,A)
        return ans

scaler = Solution()
A = [2,7,9,3,1]# ans = 12 (2,9,1)
B = [1,1,100,2,1,101]# = 202(1,100,101)
C = [1,1,100,1000,3,101]
print (scaler.solve(A))
print (scaler.solve(B))
print (scaler.solve(C))
print (scaler.solve_dp(C))
