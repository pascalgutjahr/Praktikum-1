import numpy as np
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

t, T1, T2, pa, pb, N = np.genfromtxt('tabelle.txt', unpack=True, skip_header=2)
t = t*60
T1 = T1+273.15
T2 = T2+273.15

x_plot = np. linspace(min(t), max(t))


def f(t, a, b, c):
    return a*t**2 + b*t + c

params, covariance = curve_fit(f, t, T1)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('c =', params[2], '±', errors[2])

plt.plot(x_plot, f(x_plot, *params), 'b-', label='Regression T1(t)', linewidth=1)


def g(t, d, e, f):
    return d * t**2 + e*t + f

params, covariance = curve_fit(g, t, T2)

errors = np.sqrt(np.diag(covariance))

print('d =', params[0], '±', errors[0])
print('e =', params[1], '±', errors[1])
print('f =', params[2], '±', errors[2])

plt.plot(x_plot, g(x_plot, *params), 'r-', label='Regression T2(t)', linewidth=1)

plt.plot(t, T1, 'bx', label='Temperatur 1')
plt.plot(t, T2, 'rx', label='Temperatur 2')
plt.xlabel(r'$\mathrm{t}\,/\,\mathrm{s}$')
plt.ylabel(r'$\mathrm{T}\,/\, \mathrm{K}$')
plt.xlim(min(t), max(t))
plt.legend(loc='best')
plt.grid()
plt.savefig('Bilder/Temperatur.pdf')
plt.show()
