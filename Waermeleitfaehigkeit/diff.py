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


plt.plot(t * 0.2, T7-T8, 'b-', label='$\Delta T = T7-T8$')
plt.plot(t * 0.2, T2-T1, 'r-', label='$\Delta T = T2-T1$')
plt.grid()
plt.xlim(0, 710)
#plt.ylim(20, 70)
plt.xlabel(r'$t \,/\, \mathrm{s}$')
plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
plt.title(r"Temperaturdifferenzen", **csfont)
plt.legend(loc='best')


plt.tight_layout
plt.savefig('diff.pdf')
plt.show()
