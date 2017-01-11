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

plt.subplot(2, 1, 1)
v, Uc = np.genfromtxt("tables/CSpannung.txt", unpack = True, skip_header=2)
U0 = 6.7
U = Uc/U0

# Theoriekurve
# L = 3.53 * (10**-3)
# C = 5.015 * (10**-9)
# w = v * 2 * np.pi
# R = 271.6
# U_theo = U0 / (np.sqrt((1 - L * C * (w**2)**2)+ (w**2) * (R**2) * (C**2)))
# plt.plot(v, U_theo, 'b-', label='Theoriekurve')

plt.plot(v, U, 'rx', label="Messwerte")
plt.xlabel(r'$\mathrm{\nu} \,/\, \mathrm{kHz}$')
plt.ylabel(r'$\mathrm{U_c} \,/\, \mathrm{U_0}$')
plt.xscale('log')
plt.legend(loc='best')
plt.grid()


plt.subplot(2, 1, 2)
plt.plot(v, U, 'kx', label="Messwerte")
plt.plot((32.196, 32.196), (1.5, 3.0), 'g--', label='Breite der Resonanzkurve')
plt.plot((44.442, 44.442), (1.5, 3.0), 'g--')
plt.xlim(28, 52)
plt.ylim(1.3, 3.5)
plt.xlabel(r'$\mathrm{\nu} \,/\, \mathrm{kHz}$')
plt.ylabel(r'$\mathrm{U_c} \,/\, \mathrm{U_0}$')
plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()
plt.savefig('Bilder/UcUv.pdf')
plt.show()
