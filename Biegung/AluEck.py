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

s1, a1, s2, a2 = np.genfromtxt('alu_eckig2.txt', unpack=True)

plt.subplot(2, 1, 1)
def f1(s1, m1, n1):
    return m1 * s1 + n1

params, covariance = curve_fit(f1, s1, a1)

errors = np.sqrt(np.diag(covariance))

print('m1 =', params[0], '±', errors[0])
print('n1 =', params[1], '±', errors[1])

s1_plot = np.linspace(0, 50)

plt.plot(s1, a1, 'rx', label='Aluminium eckig (von links)')
plt.plot(s1_plot, f1(s1_plot, *params), 'b-', label='linearer Fit', linewidth=3)

plt.grid()
plt.xlim(50, 30)
plt.ylim(0, 1)
plt.xlabel(r'$s \,/\, \mathrm{cm}$')
plt.ylabel(r'$a \,/\, \mathrm{mm}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')


plt.subplot(2, 1, 2)
def f2(s2, m2, n2):
    return m2 * s2 + n2

params, covariance = curve_fit(f2, s2, a2)

errors = np.sqrt(np.diag(covariance))

print('m2 =', params[0], '±', errors[0])
print('n2 =', params[1], '±', errors[1])

s2_plot = np.linspace(0, 31)
plt.plot(s2, a2, 'kx', label='Aluminium eckig (von rechts)')
plt.plot(s2_plot, f2(s2_plot, *params), 'b-', label='linearer Fit', linewidth=3)

plt.grid()
plt.xlim(7, 24)
plt.ylim(0, 1)
plt.xlabel(r'$s \,/\, \mathrm{cm}$')
plt.ylabel(r'$a \,/\, \mathrm{mm}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('FitAluEck.pdf')
plt.show()
