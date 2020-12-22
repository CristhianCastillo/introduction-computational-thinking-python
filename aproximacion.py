def run ():
    objetivo = int(input("Ingresa un numero: "))
    epsilon = 0.0001 # ¿Que tan preciso?
    paso = epsilon**2  # Aproximacion, epsilon es mas pequeño cada iteración
    respuesta = 0.0

    while abs(objetivo - respuesta**2) >= epsilon and respuesta <= objetivo:
        print(f"Valor Absoluto: {abs(respuesta**2 - objetivo)} - Respuesta {respuesta}")
        respuesta += paso
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print("No se encontro la raiz cuadrada del objetivo.")
    else:
        print(f"La raiz cuadra del {objetivo} es {respuesta}")


if __name__ == "__main__":
    run()