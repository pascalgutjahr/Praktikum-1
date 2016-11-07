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
a1 *= 1e-3
s2 *= 1e-2
a2 *= 1e-3

plt.subplot(2, 1, 1)
dia = 0.562 * (s1)**2 - (s1)**3 / 3  # Umrechnung auf andere Achsenskalierung
# dia *= 1e3


def f1(dia, m1, n1):
    return m1 * dia + n1

# m1 = -0.00513043396083 ± 0.000565678977921 -> positiv, da x-Achse von groß nach klein verläuft
# n1 = 0.000787607986555 ± 4.07550300448e-05

params, covariance = curve_fit(f1, dia, a1)

errors = np.sqrt(np.diag(covariance))


print('m1 =', params[0], '±', errors[0])
print('n1 =', params[1], '±', errors[1])
print('dia =', dia)

#  0.09571987  0.0926208   0.08953813  0.08647387  0.08343     0.08040853
#  0.07741147  0.0744408   0.07149853  0.06858667  0.0657072   0.06286213
#  0.06005347  0.0572832   0.05455333  0.05186587  0.0492228   0.04662613

s1_plot = np.linspace(min(dia), max(dia))
# spacing = 1

plt.plot(dia, a1, 'rx', label='Aluminium eckig (von links)')
plt.plot(s1_plot, f1(s1_plot, *params), 'b-', label='linearer Fit', linewidth=3)

plt.grid()
plt.xlim(max(dia)+0.0001, min(dia))
plt.xticks(np.arange(min(s1_plot), max(s1_plot), 0.005), rotation=45, rotation_mode='anchor', ha='right', va='top')  # Schritte auf x-Achse
# plt.ylim(0, 1)
plt.xlabel(r'$x \,/\, \mathrm{m}$')
plt.ylabel(r'$D(x) \,/\, \mathrm{m}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')


plt.subplot(2, 1, 2)
dia2 = 0.562 * (s2)**2 - (s2)**3 / 3  # Umrechnung auf andere Achsenskalierung
# dia2 *= 1e3

def f2(dia2, m2, n2):
    return m2 * dia2 + n2

# m2 = 0.0238651386 ± 0.00172018402974
# n2 = 6.95841784392e-05 ± 2.65805427609e-05

params, covariance = curve_fit(f2, dia2, a2)

errors = np.sqrt(np.diag(covariance))

print('m2 =', params[0], '±', errors[0])
print('n2 =', params[1], '±', errors[1])
print('dia2=', dia2)

#  0.00263947  0.00342613  0.0043092   0.00528667  0.00635653  0.0075168
#  0.00876547  0.01010053  0.01152     0.01302187  0.01460413  0.0162648
#  0.01800187  0.01981333  0.0216972   0.02365147  0.02567413  0.0277632

s2_plot = np.linspace(min(dia2), max(dia2))
plt.plot(dia2, a2, 'kx', label='Aluminium eckig (von rechts)')
plt.plot(s2_plot, f2(s2_plot, *params), 'b-', label='linearer Fit', linewidth=3)

plt.grid()
plt.xlim(min(dia2)-0.0001, max(dia2))
plt.xticks(np.arange(min(s2_plot), max(s2_plot), 0.005), rotation=45, rotation_mode='anchor', ha='right', va='top')
# plt.ylim(0, 1)
plt.xlabel(r'$x \,/\, \mathrm{m}$')
plt.ylabel(r'$D(x) \,/\, \mathrm{m}$')
plt.title(r'Aluminium, beidseitige Einspannung')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('FitAluEck.pdf')
plt.show()
