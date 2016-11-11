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

T, p = np.genfromtxt('data1.txt', unpack=True, skip_header=2)
x = np.log(p)
def f(x, m, n):
    return m * x + n

params, covariance = curve_fit(f, T, x)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

x_plot = np.linspace(min(T)-1, max(T)+1)

plt.plot(T,x, 'rx', label='bis 1bar')
plt.plot(x_plot, f(x_plot, *params),'b-', label='linearer Fit')
#plt.xlim(min(x)-1, max(x)+1)
plt.xlabel('Temperatur')
plt.ylabel('log(p)')
plt.grid()
plt.tight_layout()
plt.show()
