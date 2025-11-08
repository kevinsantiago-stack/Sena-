def generador_n(n):
    i=0
    while i<n:
        yield i; i+=1

if __name__=='__main__':
    print(list(generador_n(5)))
