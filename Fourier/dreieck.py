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

# U_mess = a_n
n, a_n = np.genfromtxt('dreieck.txt', unpack=True, skip_header=2)
x = np.log(n)
y = np.log(a_n)


def f(x, a, b):
    return a * x + b

params, covariance = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

# a = -3.05176010498 +- 0.757153910717
# b = 0.926241270667 +- 0.843097215991

# wir müssen die ungeraden Wellen betrachten!!:
# a = -2.17074020509 +- 0.627772184982
# b = 0.978614522721 +- 0.989079010416


x_plot = np.linspace(min(x), max(x))

plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(x, y, 'rx', label='Messwerte')
plt.ylabel(r'$\mathrm{log(a_n)}$')
plt.xlabel(r'$\mathrm{log(n)}$')
# plt.title('Messungen')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('bilder/dreieck.pdf')
plt.show()
