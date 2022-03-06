class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve1(self, A, B):
        N  = len(A)
        map_cords = dict()
        max_a=max(A)
        max_b = max(B)
        for i in range(1,max_a+1):
            for j in range(1,max_b+1):
                map_cords[(i,j)] =0
        for x,y in zip(A,B):
            map_cords[(x,y)] = 1
        #print(map_cords)
        cnt = 0
        for i in range(N):
            for j in range(i+1,N):
                if (A[i] != A[j]) and (B[i] != B[j]):
                    if (map_cords[(A[i],B[j])] == 1) and (map_cords[(A[j],B[i])] == 1):
                        cnt +=1
        return cnt//2



        '''
        '''
    def solve(self, A, B):
        #set implementation
        N  = len(A)
        #first storiing all coordinates in a set for O(1) access time
        coordinates = set()
        for x, y in zip(A,B):
            coordinates.add((x, y))
        cnt = 0
        for i in range(N):
            for j in range(i+1,N):
                x1,y1 = A[i],B[i]
                x2, y2 = A[j], B[j]
                if (x1 != x2) and (y1 != y2):
                    if ((x1,y2) in coordinates) and ((x2,y1) in coordinates):
                        cnt +=1
        return cnt//2




scaler = Solution()
#A = [1, 1, 2, 2]
#B = [1, 2, 1, 2]
A = [1, 1, 2, 2, 3, 3]
B = [1, 2, 1, 2, 1, 2]
print (scaler.solve( A, B))

