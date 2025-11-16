class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

kevin_santiago_larrota_cuervo = Profesor("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.agregar_materia("Matemáticas")
print(kevin_santiago_larrota_cuervo.materias)