'''
Given start and end point of maze, blocked cell, cells filled with cheese, count number of paths from start to end such that,
such that, rat can eat all cheese present in the maze wihout stpping in cell twice in sinle path.
'''

class Solution:
    def count_path(self,A,M,N,si,sj,ei,ej,total_cheese,cheese_eaten):
        if si == ei and sj == ej:
            if cheese_eaten == total_cheese:
                return 1
            else:
                return 0
        if si < 0 or sj < 0 or si > M or sj > N:
            return 0
        if A[si][sj] == 1 or A[si][sj] == -1:
            return 0
        temp = A[si][sj]
        A[si][sj] = -1
        if temp == 0:
            cheese_eaten +=1
        ans = self.count_path(A,M,N,si+1,sj,ei,ej,total_cheese,cheese_eaten) \
            + self.count_path(A,M,N,si,sj+1,ei,ej,total_cheese,cheese_eaten) \
            + self.count_path(A, M, N, si-1, sj, ei, ej, total_cheese, cheese_eaten) \
            + self.count_path(A, M, N, si, sj - 1, ei, ej, total_cheese, cheese_eaten) \

        if temp == 0:
            cheese_eaten -= 1
        A[si][sj] = temp
        return ans

    def solve(self,A,si,sj,ei,ej):
        #calculate total cheese available
        total_cheese = 0
        M = len(A)
        N = len(A[0])
        for i in range(M):
            for j in range(N):
                if A[i][j] == 0:
                    total_cheese += 1
        cheese_eaten = 0
        path = self.count_path(A,M-1,N-1,si,sj,ei,ej,total_cheese,cheese_eaten)
        return path


A = [   [3,0,0,0],
        [0,0,1,0],
        [3,0,0,0]
    ]
start = 0,0
end = 2,0
scaler = Solution()
print(scaler.solve(A,0,0,2,0))

