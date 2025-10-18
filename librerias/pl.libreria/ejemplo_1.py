from PIL import Image, ImageFilter

# Abrir una imagen
imagen = Image.open("paisaje.jpg")

# Aplicar un filtro de desenfoque
imagen_desenfocada = imagen.filter(ImageFilter.BLUR)

# Mostrar el resultado
imagen_desenfocada.show()

# Guardar la imagen procesada
imagen_desenfocada.save("paisaje_desenfocado.jpg")