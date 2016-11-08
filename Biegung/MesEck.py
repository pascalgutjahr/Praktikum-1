import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

s,a = np.genfromtxt('messing_eckig1.txt', unpack=True)
s *= 1e-2
a *= 1e-3

dia = 0.549 * (s)**2 - (s)**3 / 3


def f(dia, m, n):
    return m * dia + n

# m = 0.0817758955818 ± 0.000392863483717
# n = 8.60868605435e-05 ± 1.85997173663e-05

M = 0.0817758955818

E_2 = (0.4603 * 9.81) / (2 * 8.97e-10 * M)
print('E_2=', E_2)
# E_2= 30779547759



params, covariance = curve_fit(f, dia, a)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '±', errors[0])
print('n =', params[1], '±', errors[1])

s_plot = np.linspace(min(dia), max(dia))

plt.title(r'Messing, einseitige Einspannung')
plt.plot(dia, a, 'rx', label="Messing eckig")
plt.plot(s_plot, f(s_plot, *params), 'b-', label='linearer Ausgleich', linewidth=3)
plt.xlim(min(dia)-0.0001, max(dia)+0.0001)
plt.xlabel(r'$(Lx^2 - \frac{x^3}{3}) \,/\, \mathrm{m}$')
plt.ylabel(r'$D(x) \,/\, \mathrm{m}$')
plt.grid()

plt.legend(loc="best")
plt.tight_layout()
plt.savefig('FitMessEck.pdf')
plt.show()
