'''
Problem Description
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
Also given an integer C which represents knapsack capacity.
Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.
NOTE:
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
Problem Constraints
1 <= N <= 103
1 <= C <= 103
1 <= A[i], B[i] <= 103
Input Format
First argument is an integer array A of size N denoting the values on N items.
Second argument is an integer array B of size N denoting the weights on N items.
Third argument is an integer C denoting the knapsack capacity.
Output Format
Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.
Example Input
Input 1:
 A = [60, 100, 120]
 B = [10, 20, 30]
 C = 50
Input 2:
 A = [10, 20, 30, 40]
 B = [12, 13, 15, 19]
 C = 10
Example Output
Output 1:
 220
Output 2:
 0
Example Explanation
Explanation 1:
 Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220
Explanation 2:
 Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.
'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def knapsack(self,index,weight,A,B,C,dp):
        if index < 0 or weight == 0:
            return 0
        if dp[index][weight] != -1:
            return dp[index][weight]
        not_select = self.knapsack(index-1,weight,A,B,C,dp)
        select = 0
        if B[index] <= weight:
            select = A[index] + self.knapsack(index-1,weight-B[index],A,B,C,dp)
        dp[index][weight] = max(select,not_select)
        return dp[index][weight]

    def solve_recursive(self, A, B, C):
        N = len(A)
        dp = [[-1]*(C+1) for i in range(N+1)]
        return self.knapsack(N-1,C,A,B,C,dp)
    def solve(self,A,B,C):
        N = len(A)
        dp = [[0] * (C + 1) for i in range(N + 1)]
        for i in range(1,N+1):
            for j in range(C+1):
                if B[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j],A[i-1]+dp[i-1][j-B[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][C]

scaler = Solution()
A = [60, 100, 120]
B = [10, 20, 30]
C = 50
print(scaler.solve(A, B, C))