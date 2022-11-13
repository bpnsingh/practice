'''
Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].
Find whether the given graph is bipartite or not.
A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B
Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
Problem Constraints
1 <= A <= 100000
1 <= M <= min(A*(A-1)/2,200000)
0 <= B[i][0],B[i][1] < A
Input Format
The first argument given is an integer A.
The second argument given is the matrix B.
Output Format
Return 1 if the given graph is bipartide else return 0.
Example Input
Input 1:
A = 2
B = [ [0, 1] ]
Input 2:
A = 3
B = [ [0, 1], [0, 2], [1, 2] ]
Example Output
Output 1:
1
Output 2:
0
Example Explanation
Explanation 1:
Put 0 and 1 into 2 different subsets.
Explanation 2:
It is impossible to break the graph down to make two different subsets for bipartite matching
'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def check_bipart(self,node,adj_mat,color_set):
        Q = deque()
        Q.append(node)
        color_set[node] = 1
        while Q:
            temp = Q.popleft()
            for node in adj_mat[temp]:
                if color_set[node] == -1:
                    color_set[node] = 1 - color_set[temp]
                    Q.append(node)
                elif color_set[node] == color_set[temp]:
                    return False
        return True

    def solve(self, A, B):
        color_set = [-1]*(A)
        adj_mat = [[] for i in range(0,A)]
        for parent,child in B:
            adj_mat[parent].append(child)
            adj_mat[child].append(parent)
        #print(adj_mat)
        for i in range(A):
            if color_set[i] == -1:
                if not self.check_bipart(i,adj_mat,color_set):
                    return 0
        return 1

scaler = Solution()
A = 3
B = [ [0, 1], [0, 2], [1, 2] ]
A = 2
B = [ [0, 1] ]
A = 9
B =[
  [2, 5],
  [6, 7],
  [4, 8],
  [2, 3],
  [0, 3],
  [4, 7],
  [1, 8],
  [3, 8],
  [1, 3],
]
print(scaler.solve(A, B))
