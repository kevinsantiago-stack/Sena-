class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre; self.telefono = telefono
class Agenda:
    def __init__(self): self._contactos = []
    def agregar(self, c): self._contactos.append(c)
    def buscar(self, nombre): return [x for x in self._contactos if nombre.lower() in x.nombre.lower()]

if __name__ == '__main__':
    a = Agenda(); a.agregar(Contacto('Luis','300')); print(a.buscar('lu')[0].telefono)
