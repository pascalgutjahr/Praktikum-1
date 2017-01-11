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

# halblogarithmisch
fre, t = np.genfromtxt('tables/phase.txt', unpack=True, skip_header=2)

fre *= 1000
t /= 1e6
phirad = 2 * np.pi * fre * t

# Theoriekurve
# L = 3.53 * (10**-3)
# C = 5.015 * (10**-9)
# w = fre * 2 * np.pi
# R = 271.6
# phi = np.arctan(-(w * R * C)/(1 - (L * C * (w**2))))
#
#
# plt.plot(fre/1000, phi, 'b-', label='Theoriekurve')

plt.plot(fre/1000, phirad, 'rx', label='Messwerte')
plt.yticks(np.arange(0, 5 * np.pi/4, np.pi/4), ['$0$', '$\mathrm{\pi}/4$', '$\mathrm{\pi}/2$', '$3\mathrm{\pi}/4$','$\mathrm{\pi}$'])
plt.xscale('log')
plt.xlabel(r'$\mathrm{\nu} \,/\, \mathrm{kHz}$')
plt.ylabel(r'$\mathrm{\varphi}$')
plt.xlim()
plt.legend(loc='lower right')
plt.grid()
plt.tight_layout()
plt.savefig('Bilder/phasehalblog.pdf')
plt.show()
