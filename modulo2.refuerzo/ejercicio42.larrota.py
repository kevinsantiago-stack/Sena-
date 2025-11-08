class QueueDeque:
    def __init__(self): from collections import deque; self._d=deque()
    def enqueue(self,x): self._d.append(x)
    def dequeue(self): return self._d.popleft() if self._d else None

if __name__=='__main__':
    q=QueueDeque(); q.enqueue(1); q.enqueue(2); print(q.dequeue())
