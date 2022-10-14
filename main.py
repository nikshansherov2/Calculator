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
