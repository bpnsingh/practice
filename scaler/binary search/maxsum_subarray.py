class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    #check sum function
    def check_sum(self,A,B,K):
        sum = 0
        for i in range(K):
            sum += A[i]
        if sum > B:
            return False

        for i in range(K,len(A)):
            sum = sum + A[i] - A[i-K]
            if sum > B:
                return False
        return True

    def solve(self, A, B):
        L = 1
        R = len(A)
        ans = 0
        while L <= R:
            mid = (L + R) // 2
            if self.check_sum(A,B,mid):
                ans = mid
                L = mid+1
            else:
                R = mid - 1
        return ans




scaler = Solution()
A = [1, 2, 3, 4, 5]
B = 10
print(scaler.solve(A,B))


