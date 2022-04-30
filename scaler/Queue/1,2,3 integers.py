from collections import deque
class Queue:
    def __init__(self,array_list):
        self.buffer = deque(array_list)
    def print_items(self):
        if len(self.buffer) == 0:
            print ("Queue is empty")
            return
        for each in self.buffer:
            print (each,end=' ')
        print ()
    def add(self,val):
        self.buffer.append(val)
    def remove(self):
        return self.buffer.popleft()
    def front(self):
        return self.buffer[0]

class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        res = []
        Q = Queue([1,2,3])
        while len(res) < A:
            temp = Q.remove()
            res.append(temp)
            Q.add((temp*10)+1)
            Q.add((temp * 10) + 2)
            Q.add((temp * 10) + 3)
        return res



scaler = Solution()
print (scaler.solve(7))
