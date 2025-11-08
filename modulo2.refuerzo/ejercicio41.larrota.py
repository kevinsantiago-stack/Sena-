class StackArray:
    def __init__(self): self._arr=[]
    def push(self,x): self._arr.append(x)
    def pop(self): return self._arr.pop() if self._arr else None

if __name__=='__main__':
    s=StackArray(); s.push(1); s.push(2); print(s.pop())
