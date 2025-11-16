

class Persona:
    def actividad(self):
        print("Actividad genérica")

class Profesor(Persona):
    def actividad(self):
        print("Enseñando")

kevin_santiago_larrota_cuervo = Profesor()
kevin_santiago_larrota_cuervo.actividad()


