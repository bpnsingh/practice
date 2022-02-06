class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0, 1]
        sub_ans = self.grayCode(A - 1)
        #print(sub_ans)
        ans = []
        size = len(sub_ans)
        for i in range(size):
            ans.append(0 + sub_ans[i])
        for i in range(size-1, -1, -1):
            ans.append((1<<(A-1)) + sub_ans[i])
        return ans

scaler = Solution()
A=1
print(scaler.grayCode(A))
A=2
print(scaler.grayCode(A))
A=3
print(scaler.grayCode(A))