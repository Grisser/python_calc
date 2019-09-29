def menu_numbers():

    # Задание 4

    print("Добро пожаловать в калькулятор чисел. Вам доступны следующие функции:")
    print(" 1. Простые операции")
    print(" 2. Расширенные операции")
    print(" 3. Тригонометрические действия с градусами\n")
    type = int(input("Выберите номер действия: "))

    if type == 1:
        print(1)
    elif type == 2:
        print(2)
    elif type == 3:
        print(3)
    else:
        print("Некорректный ввод")

def main():

    pass

if __name__ == '__main__':
    main()