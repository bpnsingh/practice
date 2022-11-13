'''
You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.
Given 2 towns find whether you can reach the first town from the second without repeating any edge.
B C : query to find whether B is reachable from C.
Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).
There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i for every 1 <= i < N.
NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.
Problem Constraints
1 <= N <= 100000
Input Format
First argument is vector A
Second argument is integer B
Third argument is integer C
Output Format
Return 1 if reachable, 0 otherwise.
Example Input
Input 1:
 A = [1, 1, 2]
 B = 1
 C = 2
Input 2:
 A = [1, 1, 2]
 B = 2
 C = 1
Example Output
Output 1:
 0
Output 2:
 1
Example Explanation
Explanation 1:
 Tree is 1--> 2--> 3 and hence 1 is not reachable from 2.
Explanation 2:
 Tree is 1--> 2--> 3 and hence 2 is reachable from 1.
'''
class Solution:
    # @return an integer
    def solve(self, A, B, C):
        visited = set()
        N = len(A)
        adj_mat = {}
        for index,num in enumerate(A):
            if num not in adj_mat:
                adj_mat[num] = [index+1]
            else:
                adj_mat[num].append(index+1)
        print(adj_mat)
        def dfs(node):
            visited.add(node)
            if node not in adj_mat:
                return 0
            for path in adj_mat[node]:
                print(path,adj_mat[node])
                if path == B:
                    return 1
                if path not in visited:
                    ans = dfs(path)
                    if ans == 1:
                        return ans
            return 0
        return dfs(C)


A = [ 1, 1, 1, 3, 3, 4, 6, 5, 3, 3 ]
B = 10
C = 3
scaler = Solution()
print (scaler.solve(A,B,C))

