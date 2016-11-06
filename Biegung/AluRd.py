import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

s,a = np.genfromtxt('alu_rund1.txt', unpack=True)

def f(s, m, n):
    return m * s + n
    #m = 0.107415584417 ± 0.00239018301449
    #n = -2.04478354984 ± 0.0848991748478

params, covariance = curve_fit(f, s, a)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '±', errors[0])
print('n =', params[1], '±', errors[1])

s_plot = np.linspace(20, 45)

plt.plot(s, a, 'rx', label="example data")
plt.plot(s_plot, f(s_plot, *params), 'b-', label='linearer Ausgleich', linewidth=3)
plt.xlabel('Strecke/cm')
plt.ylabel('Auslenkung/mm')
plt.legend(loc="best")
plt.show()
