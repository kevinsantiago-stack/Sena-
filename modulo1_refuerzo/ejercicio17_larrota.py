# kevin santiago larrota cuervo
# Requiere matplotlib
import matplotlib.pyplot as plt
import os

def main():
    x = [1,2,3,4,5]
    y = [2,3,5,7,11]
    plt.figure(figsize=(6,4))
    plt.plot(x, y, marker='o')
    plt.title('Ejemplo: Serie')
    plt.xlabel('X')
    plt.ylabel('Y')
    os.makedirs('data', exist_ok=True)
    plt.savefig('data/ejemplo_plot.png')
    print('Gráfico guardado en data/ejemplo_plot.png')

if __name__ == '__main__':
    main()
