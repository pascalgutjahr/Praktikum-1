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

T1 += 273.15
T2 += 273.15
pa *= 1e5
pb *= 1e5
p0 = 5.1e5
t1 = 1/T1 * 1000
t2 = 1/T2 * 1000
x = np.log(pb/p0)
y = np.log(pa/p0)
print('pa', pa)
print('pb', pb)

# plt.subplot(2, 1, 1)


def f1(t1, a, b, ):
    return a * t1 + b

params, covariance = curve_fit(f1, t1, x)
errors = np.sqrt(np.diag(covariance))

print('a1 =', params[0], '±', errors[0])
print('b1 =', params[1], '±', errors[1])

plt.plot(t1, f1(t1, *params), 'b-', label='Ausgleichskurve 1')
plt.plot(t1, x, 'bx', label='Verdampfungswärme')
plt.xlabel(r'$\mathrm{K}\,/\,\mathrm{T}\; \cdot 10^{-3}$')
plt.ylabel(r'$\mathrm{\log\,(p_b\,/\,p_0)}$')
plt.grid()

# plt.subplot(2, 1, 2)
#
#
# def f2(t2, c, d, ):
#     return c * t2 + d
#
# params, covariance = curve_fit(f2, t2, y)
# errors = np.sqrt(np.diag(covariance))
#
# print('a2 =', params[0], '±', errors[0])
# print('b2 =', params[1], '±', errors[1])
#
# plt.plot(t2, f2(t2, *params), 'r-')
# plt.plot(t2, y, 'rx', label='Verdampfungswärme')
# plt.xlabel(r'$\mathrm{K}\,/\,\mathrm{T}\; \cdot 10^{-3}$')
# plt.ylabel(r'$\mathrm{\log\,(p_b\,/\,p_0)}$')
# plt.grid()
plt.savefig('Bilder/verdampfung.pdf')
# plt.show()
