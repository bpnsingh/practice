'''
Given a matrix of N*N find max sum of sub matarix

'''

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A):
        N = len(A)
        ans = 0
        #TL coordinates
        for i in range(0,N):
            for j in range(0,N):
                #bottom left coordinates
                for p in range(i,N):
                    for q in range(j,N):
                        sum = 0
                        for k in range(i,p+1):
                            for l in range(j,q+1):
                                sum += A[k][l]
                        ans += sum
        return ans






scaler = Solution()
A = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5],
     ]
B = 3

A = [
        [1, 1],
        [1, 1]
    ]
print (scaler.solve(A))
