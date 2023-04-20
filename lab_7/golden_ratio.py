from config import Config

def golden_ratio(a: int, b: int, eps) -> tuple:
    func = Config.our_function
    iterations = 0
    fi = 1.618  # пропорция золотого сечения
    x1 = b - (b - a) / fi
    x2 = a + (b - a) / fi

    while abs(b - a) > eps:
        if func(x1) > func(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / fi
        x2 = a + (b - a) / fi
        iterations += 1

    x = (a + b) / 2
    return round(x, 3), round(func(x), 3), f'Число итераций: {iterations}'