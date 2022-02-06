from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


class Solution:
    def solve(self, A):
        stack = Stack()
        for ch in A:
            if ch=='(' or ch=='{' or ch == '[':
                stack.push(ch)
            if ch==')' or ch=='}' or ch == ']':
                if stack.size()==0:
                    return 0
                if not is_match(ch,stack.pop()):
                    return 0

        if stack.size()==0:
            return 1
        else:
            return 0

scaler = Solution()
A="{([])}"
print (scaler.solve(A))
A = '(){'
print (scaler.solve(A))