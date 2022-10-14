def choice_num():
    txt = '''Введите
    для работы с рациональными числами: 1
    для работы с комплексными числами: 2
    для выхода: q'''
    print(txt)
    return input("Ввод: ")


def rat():
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
    return input("Ввод: ")


def comp():
    com = """Введите
    для сложения: 1
    для вычитания: 2
    для умножения: 3
    для обычного деления: 4
    для выхода: q
    для возврата в предыдущее меню: r"""
    print(com)
    return input("Ввод: ")


def r_value_1():
    return input('Enter the first number: ')


def r_value_2():
    return input('Enter the second number: ')


def с_value_1():
    valid = input('Enter the real part of first number: ')
    imaginary = input('Enter the imaginary part of first number: ')
    return tuple([valid, imaginary])


def с_value_2():
    valid = input('Enter the real part of second number: ')
    imaginary = input('Enter the imaginary part of second number: ')
    return tuple([valid, imaginary])


def sqrt_value():
    return input('Enter the first number: ')
