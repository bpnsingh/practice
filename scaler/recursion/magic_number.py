class Solution:
    # @param A : integer
    # @return an integer
    def sumofdigits(self,N):
        if N <10:
            return N
        else:
            return  N%10+self.sumofdigits(N//10)

    def solve(self, A):
        sum = self.sumofdigits(A)
        while (sum>9):
            sum = self.sumofdigits(sum)
        if sum == 1:
            return 1
        else:
            return 0






scaler = Solution()
A= 123456
print(scaler.solve(A))