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
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        cnt = 0
        Q = Queue(A)
        Q.print_items()
        #Adding all tasks under queue
        for P in B:
            while P != Q.front():
                temp = Q.remove()
                Q.add(temp)
                cnt +=1
            Q.remove()
            cnt+=1
        return cnt

scaler = Solution()
A = [2, 3, 1, 5, 4]
B = [1, 3, 5, 4, 2]
print(scaler.solve(A,B))