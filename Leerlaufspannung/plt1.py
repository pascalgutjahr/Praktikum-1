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

R, U, I = np.genfromtxt('data1.txt', unpack=True , skip_header=2)

U /=1000   # in Volt
I /=1000   # in Ampere

def f(U, m, n):
    return m * U + n

params, covariance = curve_fit(f, U, I)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

# m = -0.0612211228191 +- 0.0010219132743
# n = 0.0796268668608 +- 0.000932763635657

x_plot = np.linspace(min(U), max(U))

plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(U,I, 'rx', label='Messwerte')
plt.xlabel(r'$U /\/ \,\mathrm{V}$')
plt.ylabel(r'$I /\/ \,\mathrm{A}$')
plt.title('Messungen')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('fit1.pdf')
plt.show()
