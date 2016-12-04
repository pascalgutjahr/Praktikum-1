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

R, U, I = np.genfromtxt('recht.txt', unpack=True , skip_header=2)

U /=1000   # in Volt
I /=1000   # in Ampere

def f(I, m, n):
    return m * I + n

params, covariance = curve_fit(f, I, U)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

# m = -58.1225351417 +- 0.49383106095
# n = 0.247341114589 +- 0.000758054230739

x_plot = np.linspace(min(I), max(I))

plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(I,U, 'rx', label='Messwerte')
plt.ylabel(r'$U /\/ \,\mathrm{V}$')
plt.xlabel(r'$I /\/ \,\mathrm{A}$')
plt.title('Messungen REchteckspannung')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('recht.pdf')
plt.show()
