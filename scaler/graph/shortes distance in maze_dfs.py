'''
Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.
1 represents a wall in a matrix and 0 represents an empty location in a wall.
There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.
Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.
Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
Problem Constraints
2 <= N, M <= 100
0 <= A[i] <= 1
0 <= B[i][0], C[i][0] < N
0 <= B[i][1], C[i][1] < M
Input Format
The first argument given is the integer matrix A.
The second argument given is an array of integer B.
The third argument if an array of integer C.
Output Format
Return a single integer, the minimum distance required to reach destination
Example Input
Input 1:
A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]
Input 2:
A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]
Example Output
Output 1:
 1
Output 2:
 1
Example Explanation
Explanation 1:
 Go directly from start to destination in distance 1.
Explanation 2:
 Go directly from start to destination in distance 1.
'''
import solution as solution
from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def isValid(self, x, N):
        if x >= 0 and x < N:
            return True
        else:
            return False
    #def iswall(self,x,y,):

    def solve(self,A,B,C):
        ROWS, COLS = len(A), len(A[0])
        visited = set()
        def dfs(src,dst,dist,visited):
            print (src,dst,dist,visited)
            if src == dst:
                return True,dist
            if (src[0],src[1]) in visited:
                return False,dist
            visited.add((src[0],src[1]))
            directions = [[0, 1], [1, 0],[0, -1], [-1, 0]]
            min_path = float('inf')
            curr_path = dist
            for dr,dc in directions:
                row,col = src[0]+dr,src[1]+dc
                while self.isValid(row,ROWS) and self.isValid(col,COLS) and A[row][col] == 0:
                    curr_path += 1
                    if (row,col) not in visited:
                        isPath,curr_path = dfs((row,col),(C[0],C[1]),curr_path,visited)
                        if isPath:
                            min_path = min(min_path,curr_path)
            visited.remove((src[0],src[1]))
            if min_path != float('inf'):
                return True,min_path
            else:
                return False,min_path
        isPath,ans=dfs((B[0],B[1]),(C[0],C[1]),0,visited)
        if isPath:
            return ans
        else:
            return -1




scaler = Solution()
A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]

A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]

A =[
  [1, 1, 0, 1],
  [0, 0, 0, 1],
  [1, 0, 0, 1],
  [0, 0, 1, 0],
]
B = [ 1, 1 ]
C = [ 2, 1 ]
print(scaler.solve(A,B,C))