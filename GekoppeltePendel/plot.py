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

x, y, z = np.genfromtxt('data1.txt', unpack=True, skip_header=2)

def f(x, a, b):
    return a * x + b

params, covariance = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

x_plot = np.linspace(min(x), max(x))
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(x, y, 'rx', label='Messwerte')
plt.xlabel()
plt.ylabel()
plt.grid()
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('bilder/plot.pdf')
plt.show()
