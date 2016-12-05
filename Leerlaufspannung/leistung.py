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

R, U, I =np.genfromtxt('data1.txt', unpack=True, skip_header=2)
I/=1000
U/=1000
N = I**2 * R
R_i=16.2482145285
U0=1.2982843604
N2=(U0**2/(R_i + R)**2) *(R)
X=U/I

plt.plot(R, N, 'rx',label = 'Monozellenmessung', linewidth = 1)
plt.plot(R, N2, 'b-', label='Theoriekurve', linewidth=1)
plt.legend(loc='best')
plt.xlabel(r'$R_{a} \,/\,\ Ω $')
plt.ylabel(r'$N \,/\, \mathrm{W}$')
plt.grid()
plt.tight_layout()
plt.savefig('bilder/leistung.pdf')
plt.show()
