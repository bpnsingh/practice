'''
Problem Description
Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.
Problem Constraints
1 <= N <= 20000
1 <= A[i] <= 2000
Input Format
The first and the only argument of input contains a 2d matrix, A.
Output Format
Return an integer, representing the maximum possible sum.
Example Input
Input 1:
 A = [
        [1]
        [2]
     ]
Input 2:
 A = [
        [1, 2, 3, 4]
        [2, 3, 4, 5]
     ]
Example Output
Output 1:
 2
Output 2:
 8
Example Explanation
Explanation 1:
 We will choose 2.
Explanation 2:
 We will choose 3 and 5.
'''

'''
Approach similar to adajacent problem, but given as 2 rows of numbers,
max of numbers vertically will always be the ansers , so first we crate 
1 D array of max A , thne process the array
'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        B = []
        N = len(A[0])
        for j in range(N):
            B.append(max(A[0][j],A[1][j]))
        dp = [-1]*(N+1)
        def max_sum(index):
            if index >= N:
                return 0
            if dp[index] != -1:
                return dp[index]
            dp[index] = max(B[index] + max_sum(index+2),\
                            max_sum(index+1))
            return dp[index]
        return max_sum(0)
scaler = Solution()
A = [
        [1, 2, 3, 4],
        [2, 3, 4, 5]
     ]
A= [[1],[2]]
print (scaler.adjacent(A))
