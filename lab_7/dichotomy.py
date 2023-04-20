from config import *

def dichotomy_method(a, b, eps):
    func = Config.our_function
    global x
    d = eps
    n = 0
    while abs(b - a) >= eps:
        x = (a + b) / 2
        if func(x - d/2) > func(x + d/2):
            b = x
        else:
            a = x
        n += 2
        x = (a + b) / 2
    return round(x, 3), round(func(x), 3), f'Число итераций: {n}'
