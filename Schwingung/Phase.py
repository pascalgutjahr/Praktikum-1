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

t, U = np.genfromtxt('tables/phase.txt', unpack=True, skip_header=2)

plt.plot(t,U, 'rx', label='Messwerte')
plt.xlim(min(t), max(t))
plt.ylim(min(U), max(U))
#plt.grid()
#plt.tight_layout()
plt.show()