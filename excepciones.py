def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(20))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))