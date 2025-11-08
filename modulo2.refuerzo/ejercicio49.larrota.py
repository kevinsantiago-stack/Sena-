from enum import Enum
class Estado(Enum):
    CREADO=1; PAGADO=2; ENVIADO=3
if __name__=='__main__':
    print(list(Estado))
