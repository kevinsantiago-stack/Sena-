

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
kevin_santiago_larrota_cuervo = v1 + v2
print(kevin_santiago_larrota_cuervo)


