class Stack:
    def __init__(self): self._s = []
    def push(self,x): self._s.append(x)
    def pop(self): return self._s.pop() if self._s else None

if __name__ == '__main__':
    s = Stack(); s.push(1); s.push(2); print(s.pop())
