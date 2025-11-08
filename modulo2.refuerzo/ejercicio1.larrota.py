class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

if __name__ == "__main__":
    p = Persona("Ana", 25)
    print(p.saludar())
