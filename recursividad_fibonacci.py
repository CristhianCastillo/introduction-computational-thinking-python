def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def run():
    print(fibonacci(8))


if __name__ == "__main__":
    run()