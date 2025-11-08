class Matrix:
    def __init__(self,data): self.data=data
    def __add__(self,other):
        return Matrix([[a+b for a,b in zip(row,orow)] for row,orow in zip(self.data,other.data)])
    def __repr__(self): return str(self.data)

if __name__=='__main__':
    m1=Matrix([[1,2],[3,4]]); m2=Matrix([[5,6],[7,8]]); print(m1+m2)
