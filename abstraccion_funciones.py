# Constants
EPSILON = 0.001

# Functions
def exhaustive_search(goal):
    result = 0
    while result ** 2 < goal:
        result += 1

    if result ** 2 == goal:
        print(f"La raiz cuadrada de {goal} es {result}.")
    else:
        print(f"{goal} no tiene raiz cuadra exacta.")


def search_approximation(goal, epsilon):
    step = epsilon**2
    result = 0.0

    while abs(goal - result**2) >= epsilon and result <= goal:
        result += step

    if abs(result**2 - goal) >= epsilon:
        print("No se encontro la raiz cuadrada del objetivo.")
    else:
        print(f"La raiz cuadra de {goal} es {result}.")


def binary_search(goal, epsilon):
    low = 0.0
    high = max(1.0, goal)
    result = (high + low) / 2
    while abs(result**2 - goal) >= epsilon:
        if result**2 < goal:
            low = result
        else:
            high = result

        result = (high + low) / 2

    print(f"Al raiz cuadrada de {goal} es {result}.")


def run():
    goal = int(input("Ingresa un numero: "))
    option = int(input(f"""Selecciona uno de los siguientes metodos para intentar calcular la raiz cuadra del numero {goal}
            1. Busqueda Exaustiva, 2. Buscqueda por Aproximaciòn, 3. Busqueda Binaria
            Opcion: """))

    if option == 1:
        exhaustive_search(goal)
    elif option == 2:
        search_approximation(goal, EPSILON)
    elif option == 3:
        binary_search(goal, EPSILON)
    else:
        print("La opcion ingresada no es valida.")


if __name__ == "__main__":
    run()