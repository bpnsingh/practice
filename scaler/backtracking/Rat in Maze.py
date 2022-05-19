'''Q3. Rat In a Maze
Problem Description
 Given a grid A, a rat is at position (1, 1). He wants to go to the position (n, n) where n is size of the square matrix A.
 1 represents a traversable cell and 0 represents a non-traversable cell. Rat can only move right or down.
 Return a path that the rat can take.
   Problem Constraints
 1 <= |A| <= 4
   Input Format
 First and only argument is the vector of vectors A.
   Output Format
 Return a vector of vectors that denotes a path that can be taken.
   Example Input
 Input 1:
 A = [   [1, 0]
        [1, 1]
    ]
Input 2:
 A = [    [1, 1, 1]
         [1, 0, 1]
         [0, 0, 1]
    ]
  Example Output
 Output 1:
 [   [1, 0]
    [1, 1]
]
Output 2:
 [    [1, 1, 1]
     [0, 0, 1]
     [0, 0, 1]
]'''
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def maze_solve(self,A,N,M,x,y,path):
        #check if reached to end of maze
        if x == N and y == M:
            #it is possible that end of maze field could be blocked
            if A[x][y] == 1:
                path[x][y] = 1
                return True
            else:
                return False
        #checking boundry value
        if x < 0 or y < 0 or x > M or x > N:
            return False
        #check if field is already visited or blocked
        if A[x][y] == 0 or A[x][y] == 2:
            return False
        temp = A[x][y]
        A[x][y] = 2
        path[x][y] = 1
        if self.maze_solve(A,N,M,x+1,y,path):
            return True
        elif self.maze_solve(A,N,M,x,y+1,path):
            return True
        else:
            path[x][y] = 0
            A[x][y] = temp

    def solve(self, A):
        #input is square matrix
        N = len(A)
        path = []
        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(0)
            path.append(temp)
        self.maze_solve(A,N-1,N-1,0,0,path)
        return path


A = [
  [1, 1, 1],
  [1, 0, 1],
  [0, 0, 1]
]


scaler = Solution()
print(scaler.solve(A))