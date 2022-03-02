class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        prefix_sum = [0]*N
        prefix_sum[0] = A[0]
        for i in range(1,N):
            prefix_sum[i] = prefix_sum[i-1]+A[i]
        print (prefix_sum)
        sum = prefix_sum[0]
        if sum == B:
            return A[0:1]
        P1 = 0
        P2 = 1
        sum = prefix_sum[P2]
        while P2 < N:
            print(P1,P2,sum)
            if sum == B:
                return A[P1:P2+1]
            elif sum < B:
                P2+=1
                sum = prefix_sum[P2]
            else:
                sum = prefix_sum[P2]-prefix_sum[P1]
                P1+=1
        return -1

scaler = Solution()
A = [1,2,3,4,5]
B = 5
A = [ 5, 10, 20, 100, 105 ]
B = 110
print(scaler.solve(A,B))
