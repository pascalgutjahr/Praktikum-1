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

#  U_mess = b_n
n, b_n = np.genfromtxt('saegezahn.txt', unpack=True, skip_header=2)
x = np.log(n)
y = np.log(b_n)


def f(x, a, b):
    return a * x + b

params, covariance = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

# a = -0.997789576439 +- 0.0627097822206
# b = -0.0566750389066 +- 0.0928034543961


x_plot = np.linspace(min(x), max(x))

plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(x, y, 'rx', label='Messwerte')
plt.ylabel(r'$\mathrm{log(b_n)}$')
plt.xlabel(r'$\mathrm{log(n)}$')
# plt.title('Messungen')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('bilder/saegezahn.pdf')
plt.show()
