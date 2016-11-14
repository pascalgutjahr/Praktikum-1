import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

T, p = np.genfromtxt('data2.txt', unpack=True, skip_header=2)
# p *= 1e+5
p_0 = 995
# p_0 *= 1e+5
T = T + 273.15
T *= 1e-3
y = np.log(p/p_0)


def f(T, m, n):
    return m * T + n

params, covariance = curve_fit(f, 1/T, y)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '±', errors[0])
print('n =', params[1], '±', errors[1])

# m = -4.4413328049 ± 0.138638158231
# n = 5.68213509988 ± 0.344115696794


x_plot = np.linspace(min(1/T), max(1/T))

plt.plot(1/T, y, 'rx', label='Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit', linewidth=2)
plt.ylabel(r'$\ln(p/p_0)$')
plt.xlabel(r'$T^{-1} \ \cdot 10^{-3}\,\cdot \, \mathrm{K}$')
plt.xlim(2.29, 2.70)
plt.grid()
plt.title(r'Messung bis 15 bar')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('fit15.pdf')
plt.show()
