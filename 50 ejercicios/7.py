precio_total= 150.75
descuento= 0

if precio_total > 100:
    descuento = precio_total * 0.10
    precio_final = precio_total - descuento
    print("Precio final después del descuento es:", precio_final)
    print("Descuento aplicado:", descuento)
else:
    precio_final = precio_total
    print("No se aplicó descuento.")

print("El precio total es:", precio_total)
print("Precio final es:", precio_final)