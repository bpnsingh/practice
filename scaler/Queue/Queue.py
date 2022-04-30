from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[0]

Q=Queue()
Q.enqueue(7)
Q.enqueue(4)
Q.dequeue()
Q.enqueue(10)
Q.enqueue(20)
print(Q.front())