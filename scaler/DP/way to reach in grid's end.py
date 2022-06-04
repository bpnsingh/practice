import way as way


class Solution:
    def solve_reursion(self,A):
        N = len(A)
        M = len(A[0])
        grid = [[-1]*(M) for r in range(N)]
        def ways(x,y):
            if x == 0 and y == 0:
                return 1
            if x <0 or y<0 or A[x][y] == 0:
                return 0
            if grid[x][y] != -1:
                return grid[x][y]
            grid[x][y] = ways(x-1,y) + ways(x,y-1)
            return grid[x][y]
        ways(N-1,M-1)
        return grid[N-1][M-1]
    def solve(self,A):
        N = len(A)
        M = len(A[0])
        grid = [[0]*M for i in range(N)]
        grid[0][0] = 1

        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0 or A[i][j] == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[N-1][M-1]







A = [    [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]
scaler = Solution()
print(scaler.solve(A))