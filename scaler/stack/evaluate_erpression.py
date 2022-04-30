'''
Q1. Evaluate Expression
An arithmetic expression is given by a character array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each character may be an integer or an operator.
Input 1:
    A =   ["2", "1", "+", "3", "*"]
    op:9
'''
class Solution:
    # @param A : list of strings
    # @return an integer
    def calulate(self,operand,op1,op2):
        if operand == "/":
            return op2 // op1
        elif operand == "*":
            return op2 * op1
        elif operand == "+":
            return op2 + op1
        else:
            return op2 - op1

    def evalRPN(self, A):
        stack = []
        operators = ["+","-","/","*"]
        for item in A:
            if item in operators:
                op1 = int(stack.pop())
                op2= int(stack.pop())
                result = self.calulate(item,op1,op2)
                stack.append(result)
            else:
                stack.append(int(item))
        return stack[-1]

scaler = Solution()
A =   ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
print (scaler.evalRPN(A))

