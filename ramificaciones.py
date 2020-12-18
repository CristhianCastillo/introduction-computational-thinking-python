def run():
    num_1 = int(input("Ingresa un numero entero: "))
    num_2 = int(input("Ingresa otro numero entero: "))

    if num_1 > num_2:
        print("El primer numero es mayor que el segundo.")
    elif num_2 > num_1:
        print("El segundo numero es mayor que el primero.")
    else:
        print("Los numeros son iguales")

if __name__ == "__main__":
    run()