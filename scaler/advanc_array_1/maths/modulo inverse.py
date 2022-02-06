class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range (1,B-1):
            if (A * i) % B == 1:
                return i
        return 1
scaler = Solution()
A = 6
B = 23
print (scaler.solve(A,B))