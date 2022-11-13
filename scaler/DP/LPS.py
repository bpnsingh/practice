'''
Given a string A. Find the longest palindromic subsequence (A subsequence which does not need to be contiguous and is a palindrome).
You need to return the length of longest palindromic subsequence.
Problem Constraints
1 <= length of(A) <= 103
Input Format
First and only integer is a string A.
Output Format
Return an integer denoting the length of longest palindromic subsequence.
Example Input
Input 1:
 A = "bebeeed"
Input 2:
 A = "aedsead"
Example Output
Output 1:
 4
Output 2:
 5
Example Explanation
Explanation 1:
 The longest palindromic subsequence is "eeee", which has a length of 4.
Explanation 2:
 The longest palindromic subsequence is "aedea", which has a length of 5.
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self,A):
        N = len(A)
        dp = [[0]*(N) for i in range(N)]
        #filling diagonal
        for i in range(N):
            dp[i][i] = 1
        #length = j-i+1 ==> j = length + i -1
        #for updating second diagonal
        i = 0
        for j in range(1,N):
            if A[i] == A[j]:
                dp[i][j] = 2
            else:
                dp[i][j] = 1
            i+=1

        for length in range(2,N+1):

        return dp[0][N-1]



    def solve_recursive(self, A):
        N = len(A)
        dp = [[-1]*(N) for i in range(N)]
        def LPS(i,j):
            if i == j:
                return 1
            if i>j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if A[i] == A[j]:
                dp[i][j] = 2 + LPS(i+1,j-1)
            else:
                dp[i][j] = max(LPS(i+1,j),LPS(i,j-1))
            return dp[i][j]
        return LPS(0,N-1)
A = "bebeeed"
B = "aedsead"
scaler = Solution()
print (scaler.solve(A))