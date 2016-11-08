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

s, a = np.genfromtxt('messing_eckig1.txt', unpack=True)
s *= 1e-2
# a *= 1e-3

dia = 0.549 * (s)**2 - (s)**3 / 3
dia *= 1e+2


def f(dia, m, n):
    return m * dia + n

# Alle Angaben hier sind in den Basiseinheiten, also Metern, notiert
# m = 0.0817758955818 ± 0.000392863483717
# n = 8.60868605435e-05 ± 1.85997173663e-05

M = 0.0817758955818

E_2 = (0.4603 * 9.81) / (2 * 8.97e-10 * M)
print('E_2=', E_2)
# E_2= 30779547759

#  diese Angaben sind in cm
#  1.12275     1.26890667  1.42284333  1.58436     1.75325667  1.92933333
#  2.11239     2.30222667  2.49864333  2.70144     2.91041667  3.12537333
#  3.34611     3.57242667  3.80412333  4.041       4.28285667  4.52949333
#  4.78071     5.03630667  5.29608333  5.55984     5.82737667  6.09849333
#  6.37299     6.65066667  6.93132333  7.21476     7.50077667  7.78917333
#  8.07975

params, covariance = curve_fit(f, dia, a)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '±', errors[0])
print('n =', params[1], '±', errors[1])
print('dia=', dia)

s_plot = np.linspace(min(dia), max(dia))

plt.title(r'Messing, einseitige Einspannung')
plt.plot(dia, a, 'rx', label="Messing eckig")
plt.plot(s_plot, f(s_plot, *params), 'b-', label='linearer Ausgleich', linewidth=3)
plt.xlim(min(dia)-0.01, max(dia)+0.01)
plt.xlabel(r'$(Lx^2 - \frac{x^3}{3}) \,/\, \mathrm{cm}^3$')
plt.ylabel(r'$D(x) \,/\, \mathrm{mm}$')
plt.grid()

plt.legend(loc="best")
plt.tight_layout()
plt.savefig('FitMessEck.pdf')
plt.show()
