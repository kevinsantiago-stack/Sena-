from threading import Lock
class SafeCounter:
    def __init__(self): self._n=0; self._lock=Lock()
    def inc(self):
        with self._lock:
            self._n+=1
    def value(self): return self._n

if __name__=='__main__':
    sc=SafeCounter(); sc.inc(); print(sc.value())
