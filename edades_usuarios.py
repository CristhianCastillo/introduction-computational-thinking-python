def run ():
    user_name_1 = input("USUARIO_1: Ingresa tu nombre: ")
    user_age_1 = int(input("USUARIO_1: Ingresa tu edad: "))

    user_name_2 = input("USUARIO_2: Ingresa tu nombre: ")
    user_age_2 = int(input("USUARIO_2: Ingresa tu edad: "))

    if(user_age_1 > user_age_2):
        print(f'{user_name_1} es mayor que {user_name_2}')
    elif user_age_2 > user_age_1:
        print(f'{user_name_2} es mayor que {user_name_1}')
    else:
        print(f'{user_name_1} tiene la misma edad de {user_name_2}')

if __name__ == "__main__":
    run()