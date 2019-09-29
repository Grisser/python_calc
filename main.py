import os
import math

class Calc:

    # Задание 5

    def __init__():
        a = 0

    def str_simple():
        print('Введите строку с операцией (* или +): ', end = '')
        op = input()

        if op == '*':
            str_1 = str(input('Введите строчку, которую нужно умножить: '))
            try:
                multi_str = int(input('Введите количество повторений строки выше (число): '))
            except ValueError:
                print('Это должно быть число!')
            else:
                print(str_1*multi_str)

        elif op == '+':
            str_1 = str(input('Введите первую строку для сложения: '))
            multi_str = str(input('Введите вторую строку для сложения: '))
            print(str_1 + multi_str)

        else:
            print('Вы должны ввести "*" или "+"!')

def calc_extended():
    
    # Задание 2
    
    print("\nРасширенные операции:")
    print(" 1. Возведение в степень")
    print(" 2. Остаток от деления")
    print(" 3. Нахождение корня\n")
    definition = int(input("Выберите номер действия: "))
    
    if definition == 1:
        try:
            num = int(input("Введите число: "))
            power = int(input("Введите степень: "))
            a = num ** power
        except ValueError:
            print("Некорректный ввод")
            calc_extended()
        else:
            print("Результат: " + str(num ** power))
    elif definition == 2:
        try:
            num = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            a = num % num2
        except ValueError:
            print("Некорректный ввод")
            calc_extended()
        else:
            print("Остаток от деления: " + str(num % num2))
    elif definition == 3:
        try:
            num = int(input("Введите число: "))
            a = num ** 0.5
        except ValueError:
            print("Некорректный ввод")
            calc_extended()
        else:
            print("Результат: " + str(num ** 0.5))
    else:
        print("Некорректный ввод")
            
def calc_degrees():

    # Задание 3

    print("Если хотите посчитать синус то введите 1")
    print("Если хотите посчитать косинус то введите 2")
    a=int(input())
    if(a==1):
        print("Введите угол в градусах")
        i=int(input())
        rad=i/360*math.pi*2
        print(math.sin(rad))
    elif(a==2):
        print("Введите угол в градусах")
        i=int(input())
        rad = i / 360 * math.pi * 2
        print(math.cos(rad))
        print()
    else: print("Неверный ввод")
    calc_degrees()
            
def str_words():
    
    # Задание 6
    
    string = input("Введите строку: ")
    print(str(len(string)) + " " + str(len(string.split())))
    
def menu_numbers():

    # Задание 4

    print("Добро пожаловать в калькулятор чисел. Вам доступны следующие функции:")
    print(" 1. Простые операции")
    print(" 2. Расширенные операции")
    print(" 3. Тригонометрические действия с градусами\n")
    type = int(input("Выберите номер действия: "))

    if type == 1:
        calc_simple()
    elif type == 2:
        print(2)
    elif type == 3:
        calc_degrees()
    else:
        print("Некорректный ввод")
        
def calc_simple():
    
    # Задание 1
    
    print('+ - * /')
    print('Введите первое число')
    try:
        first = int(input())
    except ValueError:
        print('Неправильный тип вроде')
        os.abort()
    print('Введите второе число')
    try:
        second = int(input())
    except ValueError:
        print('Неправильный тип вроде')
        os.abort()
    print('Введите операцию')
    try:
        operation = input()
    except ValueError:
        print('Неправильный тип вроде')
        os.abort()
    if operation =='+':
        ravno = first + second
        print(ravno)
    elif operation =='-':
        ravno = first - second
        print(ravno)
    elif operation =='*':
        ravno = first * second
        print(ravno)
    elif operation =='/':
        try:
            ravno = first / second
        except ZeroDivisionError:
            print('Невозможно')
            print('Делить на ноль...Серьезно?')
            ravno = 42
        else:
            print(ravno)
    else:
        print('Wrong operation')      
        
def menu_strings():
    
    # Задание 7
    
    print('Добро пожаловать в калькулятор строк!')
    print('Если вы хотите совершить простые операции со строками, нажмите "1".')
    print('Если вы хотите подсчитать количество слов или символов в тексте, нажмите "2".')
    while 1 == 1:
        a = input()
        if a == '1':
            str_simple()
            pass
        elif a == '2':
            str_words()
            pass
        else:
            print('Неверный ввод. Пожалуйста, попробуйте еще раз.')
            
def menu():
    # Задание 8
    print("Привествую вас в приложении калькулятор!")
    print("Если вы хотите посчитать числа введите 1")
    print("Если вы хотите посчитать строки введите 2")
    a=int(input())
    if(a==1):
        print("Запуск калькулятора чисел") # тут должкен быть каль чисел
        menu_numbers()
        pass
    elif(a==2):
        print("Запуск калькулятора строк") # тут доложен быть каль строк
        menu_strings()
        pass
    else:
        print("Некорректный ввод")
        menu()
        pass


def main():

    pass

if __name__ == '__main__':
    main()
