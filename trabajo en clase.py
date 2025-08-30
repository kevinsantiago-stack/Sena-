lista = ["Jose", "Miguel", "Luis", "Pedro", "Pablo", "Ivan", "Juan"]
print(lista[0]) 
print(lista[5]) 
print(lista[2:5]) 
for i in lista:
    print(i)
    lista2 = lista[2:4]
    print(lista2)
    lista2 = lista[:]
    print(lista2)
    lista2 = lista[::-1]
    print(lista2) 
    lista2 = lista[-3]
    print(lista2)
lista3 = [1, 2, 5, 7, 9, 8, 10, 12, 15, 20, 30]
lista[6] = "Pepe"
print(lista)
lista.append("Pedro Pablo")
print(lista)
lista.insert(6,"Natalia")
print(lista)
lista.extend(["Jose", "Carlota", "Karen"])
print(lista)
lista.remove("Pedro")
print(lista)
lista.pop(3)
print(lista)
lista.sort()

for i in range(len(lista)):
    print(i, ":", lista[i])

lista4 =  "Perencejo" in  lista
print(lista4)
lista5 = ["a", "a", "b", "b", "c", "d", "a"]
print(lista5)
cantidad = lista5.count("b")
cantidad = lista.count("Jose")
print(lista.sort())
lista6 = sorted(lista)
print(lista6)
lista.reverse()
print(lista)
lista6 = lista.copy()
lista7 = list(lista)
print(lista6)
print(lista7)
