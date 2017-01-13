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

phi, r, T = np.genfromtxt('Idtab.txt', unpack=True, skip_header=2)
T = T**2
r *= 1e-2
r = r**2
def f(T, a, b):
    return a * T + b

params, covariance = curve_fit(f, T, r)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

x_plot = np.linspace(min(T), max(T))
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(T, r, 'rx', label='Messwerte')

plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.show()
