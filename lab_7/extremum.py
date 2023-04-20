from config import Config
from golden_ratio import *
from fibonacci import get_extremum_of_function_by_fibonacci_method
from dichotomy import *

def find_extremum():
    print("Введите отрезок [a, b]")
    a, b = [value for value in
            list(map(int, input("(2 целых числа через пробел): ").split(' ')))]
    Config.interval_start = a
    Config.interval_end = b
    print("Введите точность при нахождении экстремума")
    epsilon = float(input('>>>'))
    
    print('Введите число итераций "n" для метода Фибоначчи')
    n = int(input('>>>'))

    glr = golden_ratio(a, b, epsilon)
    fib = get_extremum_of_function_by_fibonacci_method(a, b, epsilon, n)
    dich = dichotomy_method(a, b, epsilon)
    return glr, fib, dich