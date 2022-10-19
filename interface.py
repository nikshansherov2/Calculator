import exceptions as e
import rational as r
import complex as c
import logger as l


def r_value_1():
    return input('Введите первое число: ')


def r_value_2():
    return input('Введите второе число: ')


def c_value_1():
    valid = input('Введите действительную часть первого числа: ')
    imaginary = input('Введите мнимую часть первого числа: ')
    return tuple([valid, imaginary])


def c_value_2():
    valid = input('Введите действительную часть второго числа: ')
    imaginary = input('Введите мнимую часть второго числа: ')
    return tuple([valid, imaginary])


def sqrt_value():
    return input('Введите число: ')


def for_rat(choice):
    while True:
        if choice == "8":
            num = sqrt_value()
            if e.check_num(num):
                r.init(eval(num), 0)
                res = r.do_it(choice)
                print(f"Результат: {res}")
                l.log(num, 0, res, choice)
                exit()
            else:
                print("Некорректный ввод\n")
        else:
            num_1 = r_value_1()
            num_2 = r_value_2()
            if e.check_num(num_1) and e.check_num(num_2):
                if choice in ['4', '5', '6'] and num_2 == '0':
                    print("На 0 делить нельзя\n")
                else:
                    num_1, num_2 = eval(num_1), eval(num_2)
                    r.init(num_1, num_2)
                    res = r.do_it(choice)
                    print(f"Результат: {res}\n")
                    l.log(num_1, num_2, res, choice)
                    exit()
            else:
                print("Некорректный ввод\n")


def menu_rat():
    while True:
        txt = """Введите
        для сложения: 1
        для вычитания: 2
        для умножения: 3
        для обычного деления: 4
        для деления с остатком: 5
        для деления нацело: 6
        для возведения в степень: 7
        для извлечения из квадратного корня: 8
        для выхода: q
        для возврата в предыдущее меню: r"""
        print(txt)
        choice = input("Ввод: ")
        if e.check_rat(choice):
            for_rat(choice)
        elif e.check_back(choice):
            return
        elif e.check_exit(choice):
            exit()
        else:
            print("Некорректный ввод\n")


def for_comp(choice):
    while True:
        num_1 = c_value_1()
        num_2 = c_value_2()
        if e.check_num(num_1[0]) and e.check_num(num_1[1]) and \
                e.check_num(num_2[0]) and e.check_num(num_2[1]):
            c.init_x(eval(num_1[0]), eval(num_1[1]))
            c.init_y(eval(num_2[0]), eval(num_2[1]))
            res = c.do_it(choice)
            print(f"Результат: {res}\n")
            l.log(c.x, c.y, res, choice)
            exit()
        else:
            print("Некорректный ввод\n")


def menu_comp():
    while True:
        txt = """Введите
        для сложения: 1
        для вычитания: 2
        для умножения: 3
        для обычного деления: 4
        для выхода: q
        для возврата в предыдущее меню: r"""
        print(txt)
        choice = input("Ввод: ")
        if e.check_comp(choice):
            for_comp(choice)
        elif e.check_back(choice):
            return
        elif e.check_exit(choice):
            exit()
        else:
            print("Некорректный ввод\n")


def choice_num():
    while True:
        txt = '''Введите
        для работы с рациональными числами: 1
        для работы с комплексными числами: 2
        для выхода: q'''
        print(txt)
        choice = input("Ввод: ")
        if choice == '1':
            menu_rat()
        elif choice == '2':
            menu_comp()
        elif e.check_exit(choice):
            exit()
        else:
            print("Некорректный ввод\n")
