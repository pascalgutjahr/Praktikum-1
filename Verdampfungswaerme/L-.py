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

a = 0.00924 #+- 0.0011
b = -10.86 # +- 1.4
c = 4262.7 #+- 560
d = -557950 #+- 75600
R = 8.31446
T = np.linspace(373.15, 433.15)
A = 0.9
X=(((R*T)/2*(a*T**3+b*T**2+c*T+d)) - np.sqrt((R*T)/(2*(a*T**3+b*T**2+c*T+d))**2-A/(a*T**3+b*T**2+c*T+d))) * T*(3*a*T**2 + 2*b*T + c)

plt.xlabel(r'$T \,/\,\mathrm{K}$')
plt.ylabel(r'$L\,/\, \mathrm{J/mol}$')
plt.plot(T,X,'kx', label='Messwerte')
plt.grid()
plt.tight_layout()
plt.legend()
plt.savefig('Lminus.jpg')
plt.show()
