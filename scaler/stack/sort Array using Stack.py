class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve_with_extra_stack(self, A):
        ans_stack = []
        temp_stack = []
        ans_stack.append(A[0])
        for num in A[1:]:
            while ans_stack and num > ans_stack[-1]:
                temp = ans_stack.pop()
                temp_stack.append(temp)
            ans_stack.append(num)
            while temp_stack:
                temp = temp_stack.pop()
                ans_stack.append(temp)
        return ans_stack[::-1]
    def solve(self,A):
        ans_stack = []
        ans_stack.append(A.pop())
        while A:
            temp = A.pop()
            while ans_stack and temp < ans_stack[-1]:
                temp1 = ans_stack.pop()
                A.append(temp1)
            ans_stack.append(temp)
        return ans_stack

scaler = Solution()
A = [5, 17, 100, 11]
print(scaler.solve(A))