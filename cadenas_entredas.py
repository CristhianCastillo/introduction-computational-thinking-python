def run():
    name_user = input('Ingresa tu nombre: ')
    message = f"Bienvenido {name_user} al curso de pensamiento computacion"
    print(message, f"La cadena de texto del saludo contiene: {len(message)} caracteres")


if __name__ == "__main__":
    run()