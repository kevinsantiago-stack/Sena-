class Stack:
    def __init__(self): self._s=[]
    def push(self,x): self._s.append(x)
    def pop(self): return self._s.pop() if self._s else None
    def peek(self): return self._s[-1] if self._s else None

if __name__=='__main__':
    st=Stack(); st.push(1); st.push(2); print(st.pop(), st.peek())
