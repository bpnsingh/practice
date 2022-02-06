class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        prefix_sum = [A[0]]
        for i in range(1,N):
            prefix_sum.append(prefix_sum[i-1]+A[i])
        x_max = max(prefix_sum)
        ans = B - x_max + 1
        return ans

scaler = Solution()
A = [2, 1, -3]
B = 5
print (scaler.solve(A,B))