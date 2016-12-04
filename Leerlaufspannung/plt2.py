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

R, U, I = np.genfromtxt('data2.txt', unpack=True , skip_header=2)

I /=1000   # in Ampere

def f(U, m, n):
    return m * U + n

params, covariance = curve_fit(f, U, I)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

# m = 0.0626722441168 +- 0.001489792226
# n = -0.0571161417906 +- 0.00395286541757

x_plot = np.linspace(min(U), max(U))

plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(U,I, 'rx', label='Messwerte')
plt.xlabel(r'$U \,\mathrm{V}$')
plt.ylabel(r'$I \,\mathrm{A}$')
plt.title('Messungen Gegenspannung')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('bilder/gegen.pdf')
plt.show()
