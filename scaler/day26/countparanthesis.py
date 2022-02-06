import self as self


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack_list_1 = []
        stack_list_2 = []
        for char in A:
            if char == '(':
                stack_list_1.append(char)
            if char == ')':
                stack_list_2.append(char)
        print (len(stack_list_1),len(stack_list_2))
        if len(stack_list_1) == len(stack_list_2):
            return 1
        else:
            return 0

scaler=Solution()
A = "(()())"
print (scaler.solve(A))
A = "(()"
print (scaler.solve(A))
A = "))((()(())"
print (scaler.solve(A))
