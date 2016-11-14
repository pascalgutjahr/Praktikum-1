import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (15 , 10)
plt.rcParams['font.size'] = 20
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

T, p = np.genfromtxt('data1.txt', unpack=True, skip_header=2)
#p*=1e+5
p_0 = 995
#p_0*= 1e+5
T+=273.15
T*=1e-3
x = np.log(p/p_0)

def f(T, m, n):
    return m * T + n
#m = -5.04399630475 +- 0.00587071914953
#n = 13.5372000649 +- 0.016855849829
params, covariance = curve_fit(f, 1/T, x)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

x_plot = np.linspace(min(1/T), max(1/T))

plt.plot(1/T, x, 'rx', label='Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
#plt.xlim(min(x)-1, max(x)+1)
plt.xlabel(r'$T^{-1} \ \cdot 10^{-3}\,\cdot\,\mathrm{K}$')
plt.ylabel(r'$\ln(p/p_0)$')
plt.title('Messungen bis 1 bar')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('fit1.jpg')
plt.show()
