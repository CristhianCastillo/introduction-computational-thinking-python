# def run():
#     contador = 0
#     while contador < 10:
#         print(contador)
#         contador += 1

# def run():
#     count_1 = 0
#     count_2 = 0

#     while count_1 < 10:
#         while count_2 < 5:
#             print(f'El valor del contador 1 es: {count_1} y el contador 2 es: {count_2}')
#             count_2 += 1
#         count_1 += 1
#         count_2 = 0
#         print("---------- REPITO ----------")

def run():
    count_1 = 0
    count_2 = 0

    while count_1 < 10:
        while count_2 < 5:
            if(count_2 == 3) :
                break
            print(f'El valor del contador 1 es: {count_1} y el contador 2 es: {count_2}')
            count_2 += 1
        count_1 += 1
        count_2 = 0
        print("---------- REPITO ----------")


if __name__ == "__main__":
    run()