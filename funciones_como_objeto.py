def multiplicar_por_dos(n):
    return n * 2


def sumar_dos(n):
    return n + 2


def aplicar_operaciones(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados


sumar = lambda x, y: x + y


def funciones_en_estrucuturas_datos(num):
    operaciones = [str, int, float, abs]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    
    return resultado


def run():
    numeros = [1,2,3]
    print(aplicar_operaciones(sumar_dos, numeros))
    print(aplicar_operaciones(multiplicar_por_dos, numeros))
    print(sumar(5,3))
    print(funciones_en_estrucuturas_datos(-5))


if __name__ == "__main__":
    run()