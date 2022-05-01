from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def top(self):
        return self.container[-1]
    def isempty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        #lets iterate:
        stack = Stack()
        A=A.split('/')
        for each in A:
            if each  == '' or each =='/':
                continue
            else:
                if each == '..':
                    if stack.isempty():
                        pass
                    else:
                        stack.pop()
                elif each == '.':
                    if stack.isempty():
                        pass
                    else:
                        stack.push(stack.top())
                else:
                    stack.push(each)
        if stack.isempty():
            return '/'
        else:
            return '/'+stack.top()

scaler = Solution()
A = "/../"
print (scaler.simplifyPath(A))