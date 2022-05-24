'''Given sum A, number of ways you can get that sum with dice roll[1-6].
As the number of ways can be large return its modulo by 1e9 + 7.
Problem Constraints
1 <= A <= 10 2
Input Format
The first argument is the integer A.
Output Format
Return an integer .
Example Input
Input 1:
A = 3
Input 2:
A = 4
Example Output
Output 1:
4
Output 2:
8
Example Explanation
Explanation 1:
The four possible ways to obtain 3 are: [1, 1, 1], [1, 2], [2, 1] and [3].
Explanation 2:
The eight possible ways to obrain 8 are: [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 3], [3, 1], [2, 2], [4].
'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve_dp(self, A):
        M = 10 ** 9 + 7
        if A == 0 or A == 1:
            return 1
        DP = [0]*(A+1)
        DP[0] = 1
        for i in range(A+1):
            for j in range(1,7):
                if i >= j:
                    DP[i] += DP[i-j]
                else:
                    break
        return DP[A]% M
    def solve(self,A):
        dp = [-1]*(A+1)
        def throw_dice( A):
            if A == 0:
                return 1
            if A < 0:
                return 0
            if dp[A] != -1:
                return dp[A]
            ans = 0
            for i in range(1, 7):
                if i <= A:
                    ans += self.solve(A - i)
                else:
                    break
            dp[A] = ans
            return ans
        return throw_dice(A)


scaler = Solution()
A = 4
print(scaler.solve(A))