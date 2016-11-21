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


dr, U_max = np.genfromtxt("LED.txt", unpack=True, skip_header=2)
U_max *= 1e-3
dr *= 1e-2
H = 0.06 # Messung bei Raumhelligkeit ergibt 0.06mV als Hintergrund-verstärkungsbereingt
R = 10 # kleinster Abstand zwischen LED und Diode
U = U_max - H
r = dr + R
r_2 = 1 / r**2


def f(a, r_2, b):
    return a * r_2 + b

params, covariance = curve_fit(f, r_2, U)
errors = np.sqrt(np.diag(covariance))

print("a=", params[0], "+-", errors[0])
print("b=", params[1], "+-", errors[1])


xplot = np.linspace(min(r_2),max(r_2))
plt.plot(xplot, f(xplot, *params), 'r-', label='Ausgleichskurve', linewidth=1)
plt.legend(loc="best")

plt.plot(r_2, U, "kx", label="Messwerte")
plt.xlabel(r"$ 1/r^2 \, \cdot \, (cm)^2$")
plt.ylabel(r"$U_{max} \,/\, mV$")
plt.legend(loc="best")
# plt.xlim(min(r-1),max(r+1))
# plt.ylim(0, max (U+0.5))
# plt.xticks(np.arange(min(r), max(r+1), 2.0))
# plt.yticks(np.arange(0, max(U), 0.5))
plt.grid()


plt.tight_layout()
plt.savefig("Bilder/photo1.pdf")
plt.show()
