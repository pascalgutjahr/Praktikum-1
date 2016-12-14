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

x = 2 * np.pi * t / 20

plt.plot(fre, x, 'rx', label='Messwerte')
plt.xlim(min(fre), max(fre))
# plt.ylim(min(x)-1, max(x)+1)
plt.xlabel(r'$\mathrm{\nu} \,/\, \mathrm{kHz}$')
# plt.ylabel(r'$\mathrm{t} \,/\, \mathrm{\mu} s$')
plt.xscale('log') #Funktioniert nicht!
plt.xticks(np.arange(min(fre), max(fre+1), 1.0))
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('Bilder/Phaselog.pdf')
plt.show()
