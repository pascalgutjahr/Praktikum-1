import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

T, p = np.genfromtxt('data2.txt', unpack=True, skip_header=2)
T+=273.15


# def f(p, m, n):
    # return m * p**2

# params, covariance = curve_fit(f, p, T)

# errors = np.sqrt(np.diag(covariance))

# print('m =', params[0], '±', errors[0])#
# print('n =', params[1], '±', errors[1])


# x_plot = np.linspace(min(T), max(T)+0.05)

plt.plot(T, p, 'k-', label='blaah')
#plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit', linewidth=2)

plt.grid()
plt.title(r'fehlt noch')
plt.legend(loc='best')
plt.xlabel(r'$T$')
plt.tight_layout()
plt.savefig('15.pdf')
plt.show()
