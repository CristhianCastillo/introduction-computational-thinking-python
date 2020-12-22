def factorial(n):
    """Calcula el factorial de n
    n int > 0
    returns n!
    """
    if n <= 0:
        return 0
    if n == 1:
        return n
    
    return n * factorial(n - 1)

def run():
    number = int(input("Ingresa un numero: "))
    print(f"El factorial de {number} es: {factorial(number)}")

if __name__ == "__main__":
    run()