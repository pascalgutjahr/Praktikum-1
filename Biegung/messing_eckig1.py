import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

s, a = np.genfromtxt('messing_eckig1.txt', unpack=True)

# s: Strecke, a: Biegung

plt.plot(s, a, 'kx', label='Messing eckig')
plt.grid()
plt.xlim(14, 46)
plt.ylim(0.5, 7)
plt.xlabel(r'$s \,/\, \mathrm{cm}$')
plt.ylabel(r'$a \,/\, \mathrm{mm}$')
plt.title(r'Messing eckig, einseitige Einspannung')
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('messing_eckig1.pdf')
plt.show()
