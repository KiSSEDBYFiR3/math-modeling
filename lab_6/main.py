import matplotlib.pyplot as plt
import numpy as np

from dichotomy_method import *
from functions import fun_with_param, fun
from hord_method import hord_method_with_params
from newton_method import newton_method_with_param
from iteration_method import iteration_method_with_param


def create_plot(x, y1, y2, title):
    plt.title(title)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.grid(True)
    plt.show()


# Вводим начальные значения
a = float(input("Параметр a: "))


intervalA = float(input("Левая граница интервала: "))
intervalB = float(input("Правая граница интервала: "))

# Строим график функций для наглядности
x = np.linspace(intervalA, intervalB, 1000)
y1 = fun_with_param(a, x)
y2 = fun(x)

plt.plot(x, y1)
plt.plot(x, [0 for x in x])
plt.grid(True)
plt.show()

x0 = float(input("Начальное приближение x: "))
eps = 0.001

# Узнаем количество знаков после запятой
s = str(eps)
number = abs(s.find('.') - len(s)) - 1

n = int(input("Число итераций n: "))

print("-----------------------------------------------------------------")
print("Метод дихотомии")

# Ищем приближение для функции с параметрами
dichotomy_method_with_param(eps, n, number, a, intervalA, intervalB)
# Ищем приближение для функции без параметрами
# dichotomy_method_without_param(eps, number, intervalA, intervalB)

# Показываем графики для метода дихотомии
create_plot(x, y1, [0 for xs in x], "Метод дихотомии")

print("-----------------------------------------------------------------")
print("Метод хорд")

# Ищем приближение для функции с параметрами
hord_method_with_params(x0, n, a, eps, number, intervalA, intervalB)
# Ищем приближение для функции без параметрами
# Показываем графики для метода хорд
create_plot(x, y1, [0 for x in x], "Метод хорд")

print("\n-----------------------------------------------------------------")
print("Метод простых итераций")

# Ищем приближение для функции с параметрами
iteration_method_with_param(x0, n, eps, number, a)
# Ищем приближение для функции без параметрами
# iteration_method_without_param(x0, eps, number)

# Показываем графики для метода простых итераций
create_plot(x, y1, [0 for x in x], "Метод простых итераций")

print("-----------------------------------------------------------------")
print("Метод Ньютона")

# Ищем приближение для функции с параметрами
newton_method_with_param(x0, n, a, eps, number)
# Ищем приближение для функции без параметрами
# newton_method_without_param(x0, n, eps, number)

# Показываем графики для метода Ньютона
create_plot(x, y1, [0 for x in x], "Метод Ньютона")
