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
x = np.log(p)

def f(x, m, n):
    return m * x + n

params, covariance = curve_fit(f, T, x)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '±', errors[0])
print('n =', params[1], '±', errors[1])


x_plot = np.linspace(min(T)-0.05, max(T)+0.05)

plt.plot(T, x, 'kx', label='blaah')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit', linewidth=2)

plt.grid()
plt.title(r'fehlt noch')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('fit15.pdf')
plt.show()
