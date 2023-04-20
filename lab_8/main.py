import math
import matplotlib.pyplot as plt

def f(x, y):
    a = 0.4
    b = 0.3
    l = 1.8
    n = 2
    return (-1)**n * a*y + b*(x**2) + l

# Euler method
def euler(f, x0, y0, h, x_range):
    x_list = [x0]
    y_list = [y0]
    for x in x_range:
        y = y_list[-1] + h*f(x_list[-1], y_list[-1])
        x_list.append(x + h)
        y_list.append(round(y, 6))
    return x_list, y_list


# Runge-Kutta 4th order method
def rk4(f, x0, y0, h, x_range):
    x_list = [x0]
    y_list = [y0]
    for x in x_range:
        k1 = h*f(x_list[-1], y_list[-1])
        k2 = h*f(x_list[-1] + h/2, y_list[-1] + k1/2)
        k3 = h*f(x_list[-1] + h/2, y_list[-1] + k2/2)
        k4 = h*f(x_list[-1] + h, y_list[-1] + k3)
        y = y_list[-1] + (k1 + 2*k2 + 2*k3 + k4)/6
        x_list.append(x + h)
        y_list.append(round(y, 6))
    return x_list, y_list

x_range = [i*0.2 for i in range(11)]
x0, y0 = 0, 1

# Euler's method
xe, ye = euler(f, x0, y0, 0.2, x_range)


# Runge-Kutta method
xr, yr = rk4(f, x0, y0, 0.2, x_range)

# Analytical solution
def y_analytical(x):
    return 14.875*math.exp(0.4*x) - 0.75*(x**2) - 3.75*x - 13.875

# Compare solutions
print(f"{'x':<5}{'Analytical':<15}{'Euler':<15}{'RK4':<15}")

y_plot = [1]
x_plot = [0]
for i in range(len(x_range)):
    x = x_range[i]
    y_an = y_analytical(x)
    y_plot.append(round(y_an, 6))
    x_plot.append(x)
    y_e = ye[i]
    y_r = yr[i]
    print(f"{x:<5.1f}{y_an:<15.10f}{y_e:<15.10f}{y_r:<15.10f}")


plt.plot(x_plot, y_plot, label='Exact')
plt.plot(xe, ye, label='Euler')
plt.plot(xr, yr, label='Runge-Kutta')
plt.legend()
plt.show()



