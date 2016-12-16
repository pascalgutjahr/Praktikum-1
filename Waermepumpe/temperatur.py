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

t, T1, T2, pa, pb, N = np.genfromtxt('tabelle.txt', unpack=True, skip_header=2)

x_plot = np.linspace(0, 1250)
t *= 60 # in Sekunden umgerechnet
T1 += 273.15 # in Kelvin
T2 += 273.15 # in Kelvin

def f1(t, a, b, c):
     return a * t**2 + b * t + c

params, covariance = curve_fit(f1, t, T1)
errors = np.sqrt(np.diag(covariance))

print('a1 =', params[0], '±', errors[0])
print('b1 =', params[1], '±', errors[1])
print('c1 =', params[2], '±', errors[2])
plt.plot(x_plot, f1(x_plot, *params), 'b-', label='Ausgleichskurve 1')


def f2(t, d, e, f):
    return d*t**2 + e*t + f

params, covariance = curve_fit(f2, t, T2)
errors = np.sqrt(np.diag(covariance))

print('a2 =', params[0], '±', errors[0])
print('b2 =', params[1], '±', errors[1])
print('c2 =', params[2], '±', errors[2])
plt.plot(x_plot, f2(x_plot, *params), 'r-', label='Ausgleichskurve 2')

plt.plot(t, T1, 'bx', label='Temperatur 1')
plt.plot(t, T2, 'rx', label='Temperatur 2')
plt.xlabel(r'$\mathrm{t}\,/\,\mathrm{s}$')
plt.ylabel(r'$\mathrm{T}\,/\, \mathrm{K}$')
plt.legend(loc='best')
plt.grid()
plt.show()
