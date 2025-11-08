# kevin santiago larrota cuervo
import pandas as pd

def main():
    datos = [{'producto':'A','precio':10}, {'producto':'B','precio':15}, {'producto':'C','precio':7}]
    df = pd.DataFrame(datos)
    print('DataFrame:\n', df)
    resumen = df['precio'].describe()
    print('\nResumen de precios:\n', resumen)
    df.to_csv('data/productos.csv', index=False)
    print('\nCSV guardado en data/productos.csv')

if __name__ == '__main__':
    main()
