import os

class Calc:

    # Задание 5

    def __init__(self):
        self.a = 0

    def str_simple(self):
        print('Введите строку с операцией (* или +): ', end = '')
        self.op = input()

        if self.op == '*':
            self.str_1 = str(input('Введите строчку, которую нужно умножить: '))
            try:
                self.multi_str = int(input('Введите количество повторений строки выше (число): '))
            except ValueError:
                print('Это должно быть число!')
            else:
                print(self.str_1*self.multi_str)

        elif self.op == '+':
            self.str_1 = str(input('Введите первую строку для сложения: '))
            self.multi_str = str(input('Введите вторую строку для сложения: '))
            print(self.str_1 + self.multi_str)

        else:
            print('Вы должны ввести "*" или "+"!')

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
        print(1)
    elif type == 2:
        print(2)
    elif type == 3:
        print(3)
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

def main():

    pass

if __name__ == '__main__':
    main()
