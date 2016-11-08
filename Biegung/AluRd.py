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

s, a = np.genfromtxt('alu_rund1.txt', unpack=True)
s *= 1e-2
# a *= 1e-3

dia = 0.551 * (s)**2 - (s)**3 / 3
dia *= 1e+2


def f(dia, m, n):
    return m * dia + n

# Alle Angaben hier sind in den Basiseinheiten, also Metern, notiert
# m = 0.0412361640697 ± 0.000572220500801
# n = -0.000509633620822 ± 3.21670069891e-05

M = 0.0412361640697

E_3 = (0.1209 * 9.81) / (2 * 7.187e-10 * M)
print('E_3=', E_3)
# E_2= 20009646156

params, covariance = curve_fit(f, dia, a)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '±', errors[0])
print('n =', params[1], '±', errors[1])
print('dia =', dia)

s_plot = np.linspace(min(dia), max(dia))

plt.title(r'Aluminium, einseitige Einspannung')
plt.plot(dia, a, 'rx', label="Aluminium Rund")
plt.plot(s_plot, f(s_plot, *params), 'b-', label='linearer Ausgleich', linewidth=3)
plt.xlim(min(dia)-0.0001, max(dia)+0.0001)
plt.xlabel(r'$(Lx^2 - \frac{x^3}{3}) \,/\, \mathrm{cm}$')
plt.ylabel(r'$D(x) \,/\, \mathrm{mm}$')
plt.grid()
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('FitAluRd.pdf')
plt.show()
