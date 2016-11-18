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

plt.subplot(2, 1, 1)

phi, U = np.genfromtxt('data1.txt', unpack=True, skip_header=2)

def f(phi,a, b, c, d):
    return a * phi**3 + b * phi**2 + c * phi + d

params, covariance = curve_fit(f, phi, U)

errors = np.sqrt(np.diag(covariance))

# print('a =', params[0], '±', errors[0])
# print('b =', params[1], '±', errors[1])
# print('c =', params[2], '±', errors[2])
# print('d =', params[3], '±', errors[3])
#

x_plot = np.linspace(min(phi), max(phi))



plt.plot(phi, U, 'k.', label='Ohne Rausch')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Regression', linewidth=1)

plt.ylabel(r'$U \,/\ 10^{-3} mV $')
plt.xlabel(r'${\phi}$')
plt.legend()

plt.grid()
plt.subplot(2, 1 ,2)
phi, U = np.genfromtxt('Rausch.txt', unpack=True, skip_header=2)

def f(phi,a, b, c, d):
    return a * phi**3 + b * phi**2 + c * phi + d

params, covariance = curve_fit(f, phi, U)

errors = np.sqrt(np.diag(covariance))

# print('a =', params[0], '±', errors[0])
# print('b =', params[1], '±', errors[1])
# print('c =', params[2], '±', errors[2])
# print('d =', params[3], '±', errors[3])
#

x_plot = np.linspace(min(phi), max(phi))


plt.plot(phi, U, 'k.', label='Rausch')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Regression', linewidth=1)
plt.legend()
plt.grid()






plt.show()
