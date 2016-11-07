import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

s1, a1, s2, a2 = np.genfromtxt('alu_eckig2.txt', unpack=True)

plt.subplot(2, 1, 1)
plt.plot(s2, a2, 'rx', label='Aluminium eckig (von rechts)')
plt.grid()
plt.xlim(6, 25)
plt.ylim(0, 1)
plt.xlabel(r'$s \,/\, \mathrm{cm}$')
plt.ylabel(r'$a \,/\, \mathrm{mm}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')

plt.subplot(2, 1, 2)
plt.plot(s1, a1, 'kx', label='Aluminium eckig (von links)')
plt.grid()
plt.xlim(50, 31)
plt.ylim(0, 1)
plt.xlabel(r'$s \,/\, \mathrm{cm}$')
plt.ylabel(r'$a \,/\, \mathrm{mm}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('alu_eckig2.pdf')
plt.show()
