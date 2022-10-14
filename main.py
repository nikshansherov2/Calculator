import exceptions as e
import rational as r
import complex as c
import interface as i
import logger as l


def for_rat(choice):
    num_1 = i.r_value_1()
    num_2 = i.r_value_2()
    if e.check_num(num_1) and e.check_num(num_2):

        num_1, num_2 = eval(num_1), eval(num_2)
        r.init(num_1, num_2)
        res = r.do_it(choice)
        print(f"Результат: {res}\n")
        l.log(num_1, num_2, res, choice)
    else:
        print("Некорректный ввод")
