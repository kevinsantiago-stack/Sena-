#19. Validar una contraseña (mínimo 8 caracteres, al menos una mayúscula, una minúscula y un número)

contraseña = input("Ingresa una contraseña: ")

tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False

if len(contraseña) < 8:
    print("La contraseña es demasiado corta.")
else:
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
        elif char.islower():
            tiene_minuscula = True
        elif char.isdigit():
            tiene_numero = True
    
    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        print("Contraseña válida.")
    else:
        print("La contraseña debe tener al menos una mayúscula, una minúscula y un número.")