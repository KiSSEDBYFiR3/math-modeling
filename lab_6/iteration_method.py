import matplotlib.pyplot as plt

from functions import fun_with_param, phi_with_param, phi


def iteration_method_with_param(x0, iterations, eps, number, a):
    root = phi_with_param(a, x0)
    x = x0
    n = 0
    for i in range(50):
        x = root
        root = phi_with_param(a, x)
        n += 1
        if abs(x - root) < eps:
            break
        if n == iterations: break
    print("Число итераций: ", n)
    print("X: ", round(root, number))
    y = fun_with_param(a, root)
    plt.scatter(root, y, color="red")


def iteration_method_without_param(x, eps, number):
    root = phi(x)
    n = 0
    while abs(root - x) >= eps:
        n += 1
        x = root
        root = phi(x)
    print("Число итераций: ", n)
    print("Без параметров: ", round(root, number))