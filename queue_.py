from collections import deque

class  Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()
    def isEmpty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)

q= Queue()

q.enqueue('sakib')
q.enqueue('tanbir')
q.dequeue()
q.dequeue()
print(q.isEmpty())
print(q.buffer)
