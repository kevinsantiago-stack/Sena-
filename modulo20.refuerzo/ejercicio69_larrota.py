class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_materias(self, materias):
        for m in materias:
            print(f"{self.nombre} estudia {m}")

kevin_santiago_larrota_cuervo = Alumno("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.mostrar_materias(["Matemáticas", "Física"])