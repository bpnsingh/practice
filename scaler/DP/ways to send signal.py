from sys import setrecursionlimit

setrecursionlimit(10 ** 9)


class Solution:
    # @param A : integer
    # @return an integer
    def solve_recur(self, A):
        def signal(index, prev):
            if index == A - 1:
                return 1
            way1 = way2 = 0
            if dp[index][prev] != -1:
                return dp[index][prev]
            if prev == 1:
                way1 = signal(index + 1, 0)
            else:
                way2 = signal(index + 1, 1) + signal(index + 1, 0)
            dp[index][prev] = way1 + way2
            return dp[index][prev]

        dp = [[-1] * 2 for i in range(A + 1)]
        # substituting ON --> 1 , OFF --> 0
        ans = signal(0, 1) + signal(0, 0)
        return ans % (10 ** 9 + 7)

    def solve(self, A):
        dp = [[0] * 2 for i in range(A + 1)]
        dp[1][0] = dp[1][1] = 1
        for i in range(2, A + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % (10 ** 9 + 7)
            dp[i][1] = dp[i - 1][0]
        return (dp[A][0] + dp[A][1]) % (10 ** 9 + 7)
scaler = Solution()

print(scaler.solve(3))
print(scaler.solve(4))
