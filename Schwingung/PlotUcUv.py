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

v, Uc = np.genfromtxt("tables/CSpannung.txt", unpack = True, skip_header=2)
U0 = 6.7
U = Uc/U0

plt.plot(v, U, 'rx', label="Messwerte")
plt.xscale('log')
plt.grid()
plt.tight_layout()
plt.show()