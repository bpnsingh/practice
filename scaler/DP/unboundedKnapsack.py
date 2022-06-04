'''
Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could fit in this quantity.
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
Problem Constraints
1 <= A <= 1000
1 <= |B| <= 1000
1 <= B[i] <= 1000
1 <= C[i] <= 1000
Input Format
First argument is the Weight of knapsack A
Second argument is the vector of values B
Third argument is the vector of weights C
Output Format
Return the maximum value that fills the knapsack completely
Example Input
Input 1:
A = 10
B = [5]
C = [10]
Input 2:
A = 10
B = [6, 7]
C = [5, 5]
Example Output
Output 1:
 5
Output 2:
14
Example Explanation
Explanation 1:
Only valid possibility is to take the given item.
Explanation 2:
Take the second item twice.
'''
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def knapsack(self,index,weight,A,B,dp):
        if index < 0 or weight == 0:
            return 0
        if dp[index][weight] != -1:
            return dp[index][weight]
        not_select = self.knapsack(index-1,weight,A,B,dp)
        select = 0
        if B[index] <= weight:
            select = A[index] + self.knapsack(index,weight-B[index],A,B,dp)
        dp[index][weight] = max(not_select,select)
        return dp[index][weight]

    def solve(self, A, B, C):
        N = len(A)
        weight = C
        dp = [[-1]*(C+1) for i in range(N+1)]
        return  self.knapsack(N-1,weight,A,B,dp)
scaler = Solution()
B = [20,13,10,40]
A = [100,66,40,150]
C = 50
print(scaler.solve(A, B, C))
