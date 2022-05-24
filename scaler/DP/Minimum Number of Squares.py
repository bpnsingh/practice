class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares_dp(self, A):
        dp = [A]*(A+1)
        dp[0] = 0
        for i in range(1,A+1):
            for x in range(1,i+1):
                if x*x <= i:
                    dp[i] = min(dp[i],dp[i-x*x]+1)
                else:
                    break
        return dp[A]

    def countMinSquares(self, A):
        dp = [-1]*(A+1)
        def min_square(A):
            if A <= 0:
                return 0
            if dp[A] != -1:
                return dp[A]
            ans = []
            for i in range(1,A+1):
                square = i*i
                if square <= A:
                    ans.append(min_square(A-square)+1)
                else:
                    break

            dp[A] = min(ans)
            return dp[A]
        return min_square(A)
scaler = Solution()
print(scaler.countMinSquares(20))
print(scaler.countMinSquares_dp(20))