# kevin santiago larrota cuervo
def main():
    nums = [float(input(f"Ingrese el número {i+1}: ")) for i in range(3)]
    promedio = sum(nums) / 3
    print(f"El promedio es: {promedio:.2f}")

if __name__ == '__main__':
    main()
