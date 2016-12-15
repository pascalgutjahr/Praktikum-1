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

fre, t = np.genfromtxt('tables/phase.txt', unpack=True, skip_header=2)

fre *= 1000
t /= 1e6
phirad = 2 * np.pi * fre * t


plt.plot(fre, phirad, 'rx', label='Messwerte')
# plt.xlim(min(fre), max(fre))
# plt.ylim(min(phirad)-1, max(phirad)+1)
plt.xlabel(r'$\mathrm{\nu} \,/\, \mathrm{Hz}$')
plt.ylabel(r'$\mathrm{\phi} \,/\, \mathrm{rad}$')
plt.xscale('log') # Funktioniert nicht!
# plt.xticks(np.arange(min(fre), max(fre+1), 1.0))
plt.legend(loc='best')
plt.grid()
plt.savefig('Bilder/Phaselog.pdf')
plt.show()
