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
    def is_wall(self,x,y,d,A):
        distance = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
        dx,dy = distance[d]
        if not self.isValid(x+dx,len(A)):
            return True
        if not self.isValid(y + dy,len(A[0])):
            return True
        if A[x+dx][y+dy] == 1:
            return True
        return False
    #def iswall(self,x,y,):

    def solve(self,A,B,C):
        ROWS, COLS = len(A), len(A[0])
        visited=[[ [False for col in range(4)] for col in range(COLS)] for row in range(ROWS)]
        Q = deque()
        ans = 0
        Q.append(B)
        # print (fresh)
        directions = {0:[0, 1], 1:[1, 0], 2:[0, -1], 3:[-1, 0]}
        while Q :

                r, c = Q.popleft()
                #print("starting-->{0}{1}".format(r, c))
                for d in directions:
                    dr,dc = directions[d]
                    row, col = r + dr, c + dc
                    if self.isValid(row, ROWS) and self.isValid(col, COLS) and A[row][col] == 0 and not visited[row][col][d]:
                        visited[row][col][d] = True
                        if [row,col] == B and self.is_wall(row, col,d,A):
                            print(d)
                            return ans
                        Q.append([row, col])
                ans+=1
        return ans
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