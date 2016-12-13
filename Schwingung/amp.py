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

t, U = np.genfromtxt('tables/amp.txt', unpack=True, skip_header=2)
t = t * 10**-6
def f(t, a, b):
    return a * np.exp(-2 *np.pi * b * t)
# a Maximalamplitude
# b Abklingdauer Tex
params, covariance = curve_fit(f, t, U)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

plt.plot(t, f(t, *params), 'b-', label='linearer Fit')


plt.plot(t, U, 'kx', label='Messwerte')
plt.xlabel(r'$t \,/\, s$')
plt.ylabel(r'$U \,/\, V$')
plt.legend(loc='best')
plt.grid()
plt.savefig('Bilder/amp.pdf')
plt.show()