'''
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Problem Constraints
1 <= length(A), length(B) <= 450



Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.



Output Format
Return an integer, representing the minimum number of steps required.



Example Input
Input 1:
A = "abad"
 B = "abac"
Input 2:
A = "Anshuman"
 B = "Antihuman


Example Output
Output 1:
1
Output 2:
2


Example Explanation
Exlanation 1:
A = "abad" and B = "abac"
 After applying operation: Replace d with c. We get A = B.
 
Explanation 2:
A = "Anshuman" and B = "Antihuman"
 After applying operations: Replace s with t and insert i before h. We get A = B.
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        N = len(A)
        M = len(B)
        dp = [[-1]*M for i in range(N)]
        def solve(i,j):
            if i == 0:
                return j
            if j == 0:
                return i
            if dp[i-1][j-1] != -1:
                return dp[i-1][j-1]

            if A[i-1] == B[j-1]:
                return solve(i-1,j-1)
            else:
                dp[i-1][j-1] =  min(1+solve(i-1,j-1),\
                           1+solve(i-1,j),\
                           1+solve(i,j-1) )
                return dp[i-1][j-1]
        return solve(N,M)

scaler = Solution()
A = "Anshuman"
B = "Antihuman"
A="a"
B="b"
A = "ba"
B = "aa"
A = "aaa"
B = "aa"

print (scaler.minDistance(A,B))
