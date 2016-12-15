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

# lineare Darstellung
fre, t = np.genfromtxt('tables/phase.txt', unpack=True, skip_header=2)

fre *= 1000
t /= 1e6
phirad = 2 * np.pi * fre * t


plt.plot(fre/1000, phirad, 'rx', label='Messwerte')
plt.plot((32.196, 32.196), (0.5, 2.5), 'g--', label='untere/obere Grenzfrequenz')
plt.plot((44.442, 44.442), (0.5, 2.5), 'g--')
plt.plot((36.822, 36.822), (0.5, 2.5), 'b--', label='Resonanzfrequenz')
plt.xlim(30, 45)
plt.yticks(np.arange(0, np.pi, np.pi/4), ['$0$','$\mathrm{\pi}/4$','$\mathrm{\pi}/2$', '$3\mathrm{\pi}/4$'])
# plt.ylim(min(phirad)-5, max(phirad)+5)
plt.xlabel(r'$\mathrm{\nu} \,/\, \mathrm{kHz}$')
plt.ylabel(r'$\mathrm{\varphi}$')
plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()
plt.savefig('Bilder/phaselinear.pdf')
plt.show()
