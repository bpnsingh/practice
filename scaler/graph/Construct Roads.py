'''
A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.
Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.
Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.
NOTE: All cities can be visited from any city.
Problem Constraints
1 <= A <= 105
1 <= B[i][0], B[i][1] <= N
Input Format
First argument is an integer A denoting the number of cities, N.
Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads i.e. there is a road between cities B[i][0] and B[1][1] .
Output Format
Return an integer denoting the maximum number of roads king can construct.
Example Input
Input 1:
 A = 3
 B = [
       [1, 2]
       [1, 3]
     ]
Input 2:
 A = 5
 B = [
       [1, 3]
       [1, 4]
       [3, 2]
       [3, 5]
     ]
Example Output
Output 1:
 0
Output 2:
 2
Example Explanation
Explanation 1:
 We can't construct any new roads such that the country remains bipartite.
Explanation 2:
 We can add two roads between cities (4, 2) and (4, 5).
'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        visited_color = [-1]*(A+1)
        adj_mat = [[] for i in range(A+1)]
        for parent,child in B:
            adj_mat[parent].append(child)
            adj_mat[child].append(parent)
        #print(adj_mat)
        if not B:
            return 0
        first_node = B[0][0]
        Q = deque()
        Q.append(first_node)
        visited_color[first_node] = 1
        while Q:
            temp = Q.popleft()
            for node in adj_mat[temp]:
                if visited_color[node] == -1:
                    visited_color[node] = 1 - visited_color[temp]
                    Q.append(node)
                elif visited_color[node] == visited_color[temp]:
                    return 0
        set1 = visited_color.count(1)
        set2 = visited_color.count(0)
        ans = (set1*set2) - (A-1)
        return ans%(10**9 + 7)

scaler = Solution()
A = 5
B = [
       [1, 3],
       [1, 4],
       [3, 2],
       [3, 5]
     ]
print(scaler.solve(A, B))