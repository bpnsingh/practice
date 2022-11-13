'''
Problem Description
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.
Each cell can have three values:
The value 0 representing an empty cell.
The value 1 representing a fresh orange.
The value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.
Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.
Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 2
Input Format
The first argument given is the integer matrix A.
Output Format
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.
Example Input
Input 1:
A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
Input 2:
 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]
Example Output
Output 1:
 4
Output 2:
 -1
Example Explanation
Explanation 1:
 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
Explanation 2:
 Task is impossible
'''
import solution as solution

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def isValid(self,x,N):
        if x >= 0 and x < N:
            return True
        else:
            return False
    def solve(self, A):
        Q = deque()
        ROWS,COLS = len(A),len(A[0])
        fresh, time = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if A[r][c] == 1:
                    fresh += 1
                if A[r][c] == 2:
                    Q.append([r,c])
        #print (fresh)
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        while Q and fresh > 0 :
            for i in range(len(Q)):
                r,c = Q.popleft()
                for dr,dc in directions:
                    row, col  = r + dr, c + dc
                    if self.isValid(row,ROWS) and self.isValid(col,COLS) and A[row][col]==1:
                        #print(row, col)
                        A[row][col] = 2
                        fresh -= 1
                        Q.append([row,col])
            time += 1
        return time if fresh == 0 else  -1







scaler = Solution()
A = [   [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]   ]
A = [   [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]   ]

print(scaler.solve(A))