import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

s, a = np.genfromtxt('alu_rund1.txt', unpack=True)

plt.plot(s, a, 'rx', label='Aluminium rund')
plt.grid()
plt.xlim(24, 46)
# plt.ylim()
plt.xlabel(r'$s \,/\, \mathrm{cm}$')
plt.ylabel(r'$a \,/\, \mathrm{mm}$')
plt.title(r'Aluminium rund, einseitige Einspannung')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('alu_rund1.pdf')
plt.show()
