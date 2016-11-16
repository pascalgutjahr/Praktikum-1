import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
# from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

x = np.linspace(373, 480)
# x = T ( Tmeperatur)
a = 0.00924
b = -10.86
c = 4262.7
d = -557950
R = 8.31446
A = 0.9
# L = (((R*T)/(2*(a*T**3+b*T**2+c*T+d))) + np.sqrt((R*T)/(2*(a*T**3+b*T**2+c*T+d))**2-A/(a*T**3+b*T**2+c*T+d))) * T*(3*a*T**2 + 2*b*T + c)

L = x * ((R * x)/2 + np.sqrt(((R * x)/2)**2 - A * (a * x**3 + b * x**2 + c * x + d))) * (3 * a * x**2 + 2 * b * x + c)/(a * x**3 + b * x**2 + c * x + d)
plt.xlabel(r'$T \,/\,\mathrm{K}$')
plt.ylabel(r'$L\,\cdot 10^3 \; /\, \; \mathrm{J/mol}$')
plt.plot(x, L/1000, 'k-', label='Verdampfungswärme L')
plt.xlim(min(x), max(x))
plt.grid()
plt.tight_layout()
plt.legend(loc='upper left')
plt.savefig('Lplus.jpg')
plt.show()
