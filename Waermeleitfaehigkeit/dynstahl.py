import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
# plt.rcParams['figure.figsize'] = 5, 10
csfont = {'fontname': 'Times New Roman'}

t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('dyn2.txt', unpack=True)

# plt.subplot(2, 1, 1)
plt.plot(t, T8, 'b-', label='Edelstahl außen')
plt.plot(t, T7, 'r-', label='Edelstahl innen')
plt.grid()
plt.xlim(0, 2277)
plt.xlabel(r'$t \,/\, \mathrm{s}$')
plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
plt.title(r"Edelstahl (dynamisch, $\Delta t = 2 \mathrm{s}$)", **csfont)
plt.legend(loc='best')

# plt.subplot(2, 1, 2)
# plt.plot(t, T4, 'b-', label='Messing schmal außen')
# plt.plot(t, T3, 'r-', label='Messing schmal innen')
# plt.grid()
# plt.xlim(0, 3600)
# plt.ylim(20, 70)
# plt.xlabel(r'$t \,/\, \mathrm{s}$')
# plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
# plt.title(r"Messing", **csfont)
# plt.legend(loc='best')


plt.tight_layout
plt.savefig('pl_dynstahl.pdf')
plt.show()
