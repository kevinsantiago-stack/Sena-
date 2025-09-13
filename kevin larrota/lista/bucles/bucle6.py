#invrtir una palabra si tiene mas de 5 letras
palabra = "kevin"
if len(palabra) > 5:
    invertida = ""
    for c in palabra:
        invertida = c + invertida
    print(invertida)