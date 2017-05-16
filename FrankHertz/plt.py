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

U=np.array([9.6,9.68,9.72,9.76,9.80,9.84,9.88,9.92,10])
I=np.array([0.4,0.26,0.22,0.18,0.13,0.12,0.09,0.07,0.05])
I=np.array(I)*1e-10
dI=(0.14,0.04,0.04,0.05,0.01,0.03,0.02,0.02,0.05)
dU=np.array(U)-np.array(I)
# def f(dU, m, n):
    # return m * dU + n

# params, covariance = curve_fit(f, dU, U)

# errors = np.sqrt(np.diag(covariance))

# print('m =', params[0], '+-', errors[0])
# print('n =', params[1], '+-', errors[1])

# x_plot = np.linspace(min(dU), max(dU))

# plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.plot(U,dU/dI, 'r.', label='Messwerte')
plt.xlabel(r'$U_A \,/\, \mathrm{V}$')
plt.ylabel(r'$dI_A/dU_A \,/\, \mathrm{nA/V}$')
# plt.title('Messungen')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('bilder/plt.pdf')
plt.show()
