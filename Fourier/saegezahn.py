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

n, U_ein, nu, U_mess = np.genfromtxt('saegezahn.txt', unpack=True, skip_header=2)


def f(n, a, b):
    return a * n + b

params, covariance = curve_fit(f, n, U_ein)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

# a =
# b =

x_plot = np.linspace(min(n), max(n))

plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(n, U_ein, 'rx', label='Messwerte')
plt.ylabel(r'$\mathrm{U_n} \,/\, \mathrm{U_1}$')
plt.xlabel(r'$\mathrm{Nummer der Oberwellen}$')
# plt.title('Messungen')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('bilder/saegezahn.pdf')
plt.show()
