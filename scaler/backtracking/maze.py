'''
Given maze return the path to cheese is avialble or not.
A[x][y] = 0 #valid path
A[x][y] = 1 #blocked path
'''

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def maze_solve(self,A,N,M,x,y):
        if x == N-1 and y == M-1:
            return True
        if x < 0 or y < 0 or x > M-1 or x > N-1:
            return False
        if A[x][y] == 1 or A[x][y] == 2:
            return False
        A[x][y] = 2
        return self.maze_solve(A,N,M,x+1,y)    \
                or self.maze_solve(A,N,M,x,y+1) \
                or self.maze_solve(A,N,M,x-1,y) \
                or self.maze_solve(A,N,M,x,y-1)

    def solve(self, A):
        N = len(A)
        M = len(A[0])
        return self.maze_solve(A,N,M,0,0)




A = [    [0, 0, 1],
         [1, 0, 1],
         [1, 0, 0]
    ]

B = [    [0, 1, 1],
         [1, 1, 1],
         [1, 0, 1]
    ]
scaler = Solution()
print(scaler.solve(A))
print(scaler.solve(B))