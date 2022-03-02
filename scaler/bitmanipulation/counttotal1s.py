class Solution:
    # @param A : integer
    # @return an integer
    def powerof2(self,n):
        x = 0
        while n >= (1 << x):
            x+=1
        return x-1
    def solve(self, A):
        if A in [0,1]:
            return A
        x = self.powerof2(A)
        first = x*(1<<(x-1))
        temp = A - (1<<x)
        second =  temp + 1
        ans = first + second + self.solve(temp)
        return ans

scaler = Solution()
print(scaler.solve(8))