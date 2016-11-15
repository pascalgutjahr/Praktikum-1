import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

T, p = np.genfromtxt('data2.txt', unpack=True, skip_header=2)
T += 273.15


def f(T, a, b, c, d):
    return a * T**3 + b * T**2 + c * T + d

params, covariance = curve_fit(f, T, p)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('c =', params[2], '±', errors[2])
print('d =', params[3], '±', errors[3])


x_plot = np.linspace(min(T), max(T))

plt.plot(T, p, 'rx', label='Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Regression', linewidth=1)

plt.xlabel(r'$T \,/\; \mathrm{K}$')
plt.ylabel(r'$p \; \cdot 10^5 \,/\, \mathrm{Pa}$')
plt.title('Ausgleichspolynom 3. Grades')
plt.xlim(min(T), max(T))
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('15bar.jpg')
plt.show()
