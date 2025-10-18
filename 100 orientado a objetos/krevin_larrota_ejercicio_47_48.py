#ejemplo 47  funciones

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

kevin_santiago_larrota_cuervo = Jugador("Kevin Santiago Larrota Cuervo")
mi_equipo = Equipo()
mi_equipo.agregar_jugador(kevin_santiago_larrota_cuervo)
for j in mi_equipo.jugadores:
    print(j.nombre)


#ejemplo 48  funciones

class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, aumento):
        self.velocidad += aumento

kevin_santiago_larrota_cuervo = Vehiculo("Coche", 50)
kevin_santiago_larrota_cuervo.acelerar(20)
print(kevin_santiago_larrota_cuervo.velocidad)

