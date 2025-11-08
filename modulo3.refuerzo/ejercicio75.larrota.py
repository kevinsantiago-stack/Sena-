class CombateSimple:
    def __init__(self, a, b):
        self.a = a; self.b = b
    def turno(self):
        # a and b are dicts with 'vida' and 'ataque'
        self.b['vida'] -= max(0, self.a['ataque'] - self.b.get('defensa',0))
        return self.b['vida'] <= 0

if __name__ == '__main__':
    a={'vida':100,'ataque':20}; b={'vida':50,'defensa':5}
    c = CombateSimple(a,b); print(c.turno())
