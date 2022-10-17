import exceptions as e
import rational as r
import complex as c
import interface as i
import logger as l


def for_rat(choice):
    if choice == "8":
        num = i.sqrt_value()
        if e.check_num(num):
            r.init(eval(num), 0)
            res = r.do_it(choice)
            print(f"Результат: {res}")
            l.log(num, 0, res, choice)
        else:
            print("Некорректный ввод")
    else:
        num_1 = i.r_value_1()
        num_2 = i.r_value_2()
        if e.check_num(num_1) and e.check_num(num_2):
            if choice in ['4', '5', '6'] and num_2 == '0':
                print("На 0 делить нельзя")
            else:
                num_1, num_2 = eval(num_1), eval(num_2)
                r.init(num_1, num_2)
                res = r.do_it(choice)
                print(f"Результат: {res}\n")
                l.log(num_1, num_2, res, choice)
        else:
            print("Некорректный ввод")


def for_comp(choice):
    num_1 = i.c_value_1()
    num_2 = i.c_value_2()
    if e.check_num(num_1[0]) and e.check_num(num_1[1]) and \
            e.check_num(num_2[0]) and e.check_num(num_2[1]):
        c.init_x(eval(num_1[0]), eval(num_1[1]))
        c.init_x(eval(num_2[0]), eval(num_2[1]))
        res = r.do_it(choice)
        print(f"Результат: {res}\n")
        l.log(c.x, c.y, res, choice)


while True:
    choice_1 = i.choice_num()
    if choice_1 == "1":
        choice_2 = i.rat()
        if e.check_rat(choice_2):
            for_rat(choice_2)
        elif e.check_back(choice_2):
            continue
        elif e.check_exit(choice_2):
            break
        else:
            print("Некорректный ввод")
    elif choice_1 == "2":
        choice_2 = i.comp()
        if e.check_comp(choice_2):
            for_comp(choice_2)
        elif e.check_back(choice_2):
            continue
        elif e.check_exit(choice_2):
            break
        else:
            print("Некорректный ввод")
    elif e.check_exit(choice_1):
        break
    else:
        print("Некорректный ввод")
        continue