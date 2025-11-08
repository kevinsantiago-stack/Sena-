# kevin santiago larrota cuervo
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        cat = 'Bajo peso'
    elif imc < 25:
        cat = 'Peso normal'
    elif imc < 30:
        cat = 'Sobrepeso'
    else:
        cat = 'Obesidad'
    return round(imc, 2), cat

def main():
    imc, categoria = calcular_imc(70, 1.75)
    print(f'IMC: {imc} - {categoria}')

if __name__ == '__main__':
    main()
