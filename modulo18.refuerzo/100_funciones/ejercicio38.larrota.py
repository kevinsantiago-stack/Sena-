

def factoriales_lista(kevin_santiago_larrota_cuervo_n):
    def factorial(n):
        return 1 if n==0 else n*factorial(n-1)
    return [factorial(i) for i in range(kevin_santiago_larrota_cuervo_n+1)]

print(factoriales_lista(5))



def contar_letras_lista(kevin_santiago_larrota_cuervo_lista):
    return [len(p) for p in kevin_santiago_larrota_cuervo_lista]

print(contar_letras_lista(["Kevin","Santiago","Cuervo"]))