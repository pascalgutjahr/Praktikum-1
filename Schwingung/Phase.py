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

plt.plot(fre, t, 'rx', label='Messwerte')
plt.xlim(min(fre), max(fre))
plt.ylim(min(t), max(t)+5)
plt.xlabel(r'$f \,/\, kHz$')
plt.ylabel(r'$t \,/\, micro s$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.show()
