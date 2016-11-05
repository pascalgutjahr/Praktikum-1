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

t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('dyn1.txt', unpack=True)

# plt.subplot(2, 1, 1)
plt.plot(t*0.5, T5, 'b-', label='Aluminium außen')
plt.plot(t*0.5, T6, 'r-', label='Aluminium innen')
plt.grid()
plt.xlim(0, 1010)
plt.xlabel(r'$t \,/\, \mathrm{s}$')
plt.ylabel(r'$T \,/\,^{\circ} \mathrm{C}$')
plt.title(r"Aluminium (dynamisch $[80 \mathrm{s}]$, $\Delta t = 2 \mathrm{s}$)", **csfont)
plt.legend(loc='best')



plt.tight_layout
plt.savefig('alu_dyn1.pdf')
plt.show()
