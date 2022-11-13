'''
Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.
You have to find an integer array D of size A such that:
=> D[i] : Shortest distance form the C node to node i.
=> If node i is not reachable from C then -1.
Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
Problem Constraints
1 <= A <= 1e5
0 <= B[i][0],B[i][1] < A
0 <= B[i][2] <= 1e3
0 <= C < A
Input Format
The first argument given is an integer A, representing the number of nodes.
The second argument given is the matrix B of size M x 3, where nodes B[i][0] and B[i][1] are connected with an edge of weight B[i][2].
The third argument given is an integer C.
Output Format
Return the integer array D.
Example Input
Input 1:
A = 6
B = [   [0, 4, 9]
        [3, 4, 6] 
        [1, 2, 1] 
        [2, 5, 1] 
        [2, 4, 5] 
        [0, 3, 7] 
        [0, 1, 1] 
        [4, 5, 7] 
        [0, 5, 1] ] 
C = 4
Input 2:
A = 5
B = [   [0, 3, 4]
        [2, 3, 3] 
        [0, 1, 9] 
        [3, 4, 10] 
        [1, 3, 8]  ] 
C = 4
Example Output
Output 1:
D = [7, 6, 5, 6, 0, 6]
Output 2:
D = [14, 18, 13, 10, 0]
Example Explanation
Explanation 1:
 All Paths can be considered from the node C to get shortest path
Explanation 2:
 All Paths can be considered from the node C to get shortest path
'''
import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        #create adjancent matrix
        adj_mat = {}
        for node1,node2,weight in B:
            if node1 not in adj_mat:
                adj_mat[node1] = [(node2,weight)]
            else:
                adj_mat[node1].append((node2,weight))
        min_heap = []
        ans = [float('inf')]*A
        ans[C] = 0
        #store first adjacent neibor in min_heap
        if C in adj_mat:
            for node,weight in adj_mat[C]:
                ans[node] = weight
                heapq.heappush(min_heap,(weight,node))
            #proces minheap
        print(adj_mat)
        while min_heap:
            weight1,node1 = heapq.heappop(min_heap)
            print(weight1,node1)
            for node2,weight2 in adj_mat[node1]:
                weight = weight1 + weight2
                if weight < ans[node2]:
                    ans[node2] = weight
                    heapq.heappush(min_heap,(weight,node2))
        return ans





scaler = Solution()
'''
A = 6
B = [   [0, 4, 9],
        [3, 4, 6] ,
        [1, 2, 1] ,
        [2, 5, 1] ,
        [2, 4, 5] ,
        [0, 3, 7] ,
        [0, 1, 1] ,
        [4, 5, 7] ,
        [0, 5, 1] ]
C = 4'''
A = 5
B = [
  [0, 3, 4],
  [2, 3, 3],
  [0, 1, 9],
  [3, 4, 10],
  [1, 3, 8],
]
C = 4
print(scaler.solve(A,B,C))


