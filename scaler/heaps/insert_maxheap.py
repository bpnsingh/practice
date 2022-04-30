import heapq
'''
Inserting value in max heap
'''
class maxheap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        size = len(self.heap)
        if size == 1:
            return
        i = size - 1
        while i > 0:
            parent = (i-1)//2
            if self.heap[parent] < self.heap[i]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[i]
                self.heap[i] = temp
                i = parent
            else:
                break

scaler = maxheap()
A= [5,7,9,1,3]
for num in A:
    #print(num)
    scaler.insert(num)
    #print(scaler.heap)
print(scaler.heap)
res= []
for num in A:
    heapq.heappush(res,-1*num)
print(res)
#print(A)