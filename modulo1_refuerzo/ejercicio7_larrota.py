# kevin santiago larrota cuervo
def main():
    persona = {'nombre': 'Ana', 'edad': 28, 'ciudad': 'Madrid'}
    persona['telefono'] = '+34 123 456 789'
    print('Nombre:', persona.get('nombre'))
    print('Teléfono:', persona.get('telefono', 'No disponible'))

    empresa = {
        'nombre': 'TechCorp',
        'empleados': {
            'ana': {'puesto': 'Desarrolladora', 'salario': 45000},
            'carlos': {'puesto': 'Diseñador', 'salario': 40000}
        }
    }
    total = sum(e['salario'] for e in empresa['empleados'].values())
    print('Salario total empleados:', total)

if __name__ == '__main__':
    main()
