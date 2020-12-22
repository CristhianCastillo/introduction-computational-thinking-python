def run():
    objetivo = int(input("Ingresa un numero: "))
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    print(f"Bajo: {bajo} - Alto: {alto} - Respuesta: {respuesta}")  
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f"Bajo: {bajo} - Alto: {alto} - Respuesta: {respuesta}")
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f"Al raiz cuadrada de {objetivo} es {respuesta}")


if __name__ == "__main__":
    run()