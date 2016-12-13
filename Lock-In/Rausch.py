import numpy as np
# import uncertainties.unumpy as unp
# from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

plt.subplot(2, 1, 1)

phi, Delta_phi, U_max = np.genfromtxt('data1.txt', unpack=True, skip_header=3)
# in Bogenmaß umrechnen:
Delta_phi_B = Delta_phi * 2 * np.pi / 360
x = np.cos(Delta_phi_B)


def f(x, a, b):
    return a * x + b

params, covariance = curve_fit(f, x, U_max)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
# print('x = ', covariance)

x_plot = np.linspace(min(x), max(x))

plt.plot(x, U_max, 'k.', label='Ohne Rauschen')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.ylabel(r'$U_{max} \,/\, mV$')
plt.xlabel(r'$\cos{{(\Delta\phi)}}$')
plt.legend(loc='best')
plt.grid()



plt.subplot(2, 1, 2)

phi2, Delta_phi2, U2_max = np.genfromtxt('Rausch.txt', unpack=True, skip_header=2)
Delta_phi2_B = Delta_phi2 * 2 * np.pi / 360
x2 = np.cos(Delta_phi2_B)


def f(x2, c, d):
    return c * x2 + d

params, covariance = curve_fit(f, x2, U2_max)

errors = np.sqrt(np.diag(covariance))

print('c =', params[0], '±', errors[0])
print('d =', params[1], '±', errors[1])

x2_plot = np.linspace(min(x2), max(x2))

plt.plot(x2, U2_max, 'k.', label='mit Rauschen')
plt.plot(x2_plot, f(x2_plot, *params), 'b-', label='linearer Fit')
plt.ylabel(r'$U_{max} \, \cdot 10^{-1} \,/\, mV$')
plt.xlabel(r'$\cos{{(\Delta\phi)}}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('Bilder/phi.pdf')
plt.show()
