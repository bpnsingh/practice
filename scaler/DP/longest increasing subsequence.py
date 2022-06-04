'''
Find the longest increasing subsequence of a given array of integers, A.
In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.
In this case, return the length of the longest increasing subsequence.
Problem Constraints
1 <= length(A) <= 2500
0 <= A[i] <= 2500
Input Format
The first and the only argument is an integer array A.
Output Format
Return an integer representing the length of the longest increasing subsequence.
Example Input
Input 1:
 A = [1, 2, 1, 5]
Input 2:
 A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Example Output
Output 1:
 3
Output 2:
 6
Example Explanation
Explanation 1:
 The longest increasing subsequence: [1, 2, 5]
Explanation 2:
 The possible longest increasing subsequences: [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self,index, prev_index, A,dp):
        N = len(A)
        # print(index)
        if index == N:
            return 0
        if dp[index][prev_index + 1] != -1:
            return dp[index][prev_index + 1]
        ans = self.solve(index + 1, prev_index,A,dp)
        if prev_index == -1 or A[index] > A[prev_index]:
            prev_index = index
            ans = max(ans, 1 + self.solve(index + 1, prev_index, A,dp))
        dp[index][prev_index + 1] = ans
        return ans

    def lis(self,A):
        N = len(A)
        dp= [[-1]*(N+1) for i in range (N+1)]
        prev_index = -1
        return  self.solve(0,prev_index,A,dp)


scaler = Solution()
A= [1, 2, 1, 5]
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(scaler.lis(A))

