import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
#plt.rcParams['figure.figsize'] = 5, 10
csfont = {'fontname': 'Times New Roman'}

t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('statisch.txt', unpack=True)

plt.subplot(2, 1, 1)
plt.plot(t*0.2, T1, 'b-', label='Messing breit außen')
plt.plot(t*0.2, T2, 'r-', label='Messing breit innen')
plt.grid()
plt.xlim(0, 710)
plt.xlabel(r'$t \,/\, \mathrm{s}$')
plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
plt.title(r"Messing (statisch, $\Delta t = 5 \mathrm{s}$)", **csfont)
plt.legend(loc='best')

plt.subplot(2, 1, 2)
plt.plot(t*0.2, T4, 'b-', label='Messing schmal außen')
plt.plot(t*0.2, T3, 'r-', label='Messing schmal innen')
plt.grid()
plt.xlim(0, 710)
plt.ylim(20, 70)
plt.xlabel(r'$t \,/\, \mathrm{s}$')
plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
plt.title(r"Messing (statisch, $\Delta t = 5 \mathrm{s}$)", **csfont)
plt.legend(loc='upper left')

# wenn man 4 Graphiken zeichnen möchte: (x, y, z): x = Anzahl der Zeilen, y = Anzahl der Spalten, z = der jeweilige Platz
# plt.subplot(2, 2, 3)
# plt.plot(t, T1, 'b-', label='Messing breit außen')
# plt.plot(t, T2, 'r-', label='Messing breit innen')
# plt.grid()
# plt.xlim(0, 3600)
# plt.xlabel(r'$t \,/\, \mathrm{s}$')
# plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
# plt.title(r"Test", **csfont)
# plt.legend(loc='best')

# plt.subplot(2, 2, 4)
# plt.plot(t, T4, 'b-', label='Messing schmal außen')
# plt.plot(t, T3, 'r-', label='Messing schmal innen')
# plt.grid()
# plt.xlim(0, 3600)
# plt.ylim(20, 70)
# plt.xlabel(r'$t \,/\, \mathrm{s}$')
# plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
# plt.title(r"Test", **csfont)
# plt.legend(loc='best')


plt.tight_layout
plt.savefig('mess_stat.pdf')
plt.show()
