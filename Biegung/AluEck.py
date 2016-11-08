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

s1, a1, s2, a2 = np.genfromtxt('alu_eckig2.txt', unpack=True)
s1 *= 1e-2
# a1 *= 1e-3
s2 *= 1e-2
# a2 *= 1e-3

plt.subplot(2, 1, 1)
# Umrechnung auf andere Achsenskalierung
dia = 3 * 0.562**2 * (s1) - (4 * (s1)**3)
dia *= 1e+2


def f1(dia, m1, n1):
    return m1 * dia + n1

# Alle Angaben hier sind in den Basiseinheiten, also Metern, notiert
# m1 = 0.00126175282492 ± 0.000214805557831
# n1 = 0.000293692095235 ± 2.54720640488e-05

params, covariance = curve_fit(f1, dia, a1)

errors = np.sqrt(np.diag(covariance))


print('m1 =', params[0], '±', errors[0])
print('n1 =', params[1], '±', errors[1])
print('dia =', dia)

# -0.00630532  0.01244736  0.03004804  0.04652072  0.0618894   0.07617808
#  0.08941076  0.10161144  0.11280412  0.1230128   0.13226148  0.14057416
#  0.14797484  0.15448752  0.1601362   0.16494488  0.16893756  0.17213824

s1_plot = np.linspace(min(dia)-0.05, max(dia)+0.05)
# spacing = 1

plt.plot(dia, a1, 'rx', label='Aluminium eckig (von links)')
plt.plot(s1_plot, f1(s1_plot, *params), 'b-', label='linearer Fit', linewidth=3)

plt.grid()
plt.xlim(min(dia)-0.05, max(dia)+0.05)
# plt.xticks(np.arange(min(s1_plot), max(s1_plot), 0.005), rotation=45, rotation_mode='anchor', ha='right', va='top')  # Schritte auf x-Achse
# plt.ylim(0, 1)
plt.xlabel(r'$(3L^2x - 4x^3) \,/\, \mathrm{cm}^3$')
plt.ylabel(r'$D(x) \,/\, \mathrm{mm}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')


plt.subplot(2, 1, 2)
# Umrechnung auf andere Achsenskalierung
dia2 = 3 * 0.562**2 * (s2) - (4 * (s2)**3)
dia2 *= 1e2


def f2(dia2, m2, n2):
    return m2 * dia2 + n2

# Alle Angaben hier sind in den Basiseinheiten, also Metern, notiert
# m2 = 0.00496407560258 ± 0.000730818491117
# n2 = -0.000241932809024 ± 9.59644334768e-05

M = (0.00126175282492 + 0.00496407560258) / 2

E_1 = (0.1671 * 9.81) / (48 * 8.63e-10 * M)
print('E_1=', E_1)
# E_1= 12712362593

params, covariance = curve_fit(f2, dia2, a2)

errors = np.sqrt(np.diag(covariance))

print('m2 =', params[0], '±', errors[0])
print('n2 =', params[1], '±', errors[1])
print('dia2=', dia2)

# 0.06495524  0.07375456  0.08236188  0.0907532   0.09890452  0.10679184
# 0.11439116  0.12167848  0.1286298   0.13522112  0.14142844  0.14722776
# 0.15259508  0.1575064   0.16193772  0.16586504  0.16926436  0.17211168

s2_plot = np.linspace(min(dia2)-0.05, max(dia2)+0.05)
plt.plot(dia2, a2, 'kx', label='Aluminium eckig (von rechts)')
plt.plot(s2_plot, f2(s2_plot, *params), 'b-', label='linearer Fit', linewidth=3)

plt.grid()
plt.xlim(min(dia2)-0.05, max(dia2)+0.05)
# plt.xticks(np.arange(min(s2_plot), max(s2_plot), 0.005), rotation=45, rotation_mode='anchor', ha='right', va='top')
# plt.ylim(0, 1)
plt.xlabel(r'$(3L^2x - 4x^3) \,/\, \mathrm{cm}^3$')
plt.ylabel(r'$D(x) \,/\, \mathrm{mm}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('FitAluEck.pdf')
plt.show()
