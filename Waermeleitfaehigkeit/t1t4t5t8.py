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
plt.plot(t*0.2, T4, 'r-', label='Messing schmal außen')
plt.grid()
plt.xlim(0, 710)
plt.ylim(20, 55)
plt.xlabel(r'$t \,/\, \mathrm{s}$')
plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
plt.title(r"Messing (statisch, $\Delta t = 5 \mathrm{s}$)", **csfont)
plt.legend(loc='upper left')

plt.subplot(2, 1, 2)
plt.plot(t*0.2, T5, 'b-', label='Aluminium außen')
plt.plot(t*0.2, T8, 'r-', label='Edelstahl außen')
plt.grid()
plt.xlim(0, 710)
plt.ylim(20, 55)
plt.xlabel(r'$t \,/\, \mathrm{s}$')
plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
plt.title(r"Aluminium / Edelstahl (statisch, $\Delta t = 5 \mathrm{s}$)", **csfont)
plt.legend(loc='best')


plt.tight_layout
plt.savefig('T1T4T5T8.pdf')
plt.show()
