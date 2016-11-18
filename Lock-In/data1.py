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


phi, U = np.genfromtxt('data1.txt', unpack=True, skip_header=2)

plt.plot(phi, U, 'b-', label='Ohne Rausch')
plt.ylabel(r'$U \,/\ 10^{-3} mV $')
plt.xlabel(r'${\phi}$')
plt.grid()
plt.legend()

plt.savefig('ORausch.jpg')
plt.show()
