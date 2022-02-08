class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return ['0', '1']
        sub_ans = self.grayCode(A - 1)
        #print(sub_ans)
        ans = ''
        size = len(sub_ans)
        for i in range(size):
            ans = '0'+str(ans)
        for i in range(size-1, -1, -1):
            ans = '1' + str(ans)
        return ans

scaler = Solution()
A=1
print(scaler.grayCode(A))
A=2
print(scaler.grayCode(A))
A=3
print(scaler.grayCode(A))