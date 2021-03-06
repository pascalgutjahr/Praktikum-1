import matplotlib as mpl
from scipy.optimize import curve_fit
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.rcParams['lines.linewidth'] = 1
import numpy as np
#from curve_fit import ucurve_fit

mpl.rcParams.update({
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}'
})

dr, U_max = np.genfromtxt("LED.txt", unpack=True, skip_header=2)
H = 0.06 # Messung bei Raumhelligkeit ergibt 0.06mV als Hintergrund-verstärkungsbereingt
R = 10 # kleinster Abstand zwischen LED und Diode
U = U_max - H
r = dr + R


def f(r, a, b, c):
    return a + b/(r+c)**2

# a= -0.0271172990579 +- 0.00493203668317
# b= 69.2408025162 +- 2.42624318655
# c= -4.22456714135 +- 0.104653712933

params, covariance = curve_fit(f, r, U)
errors = np.sqrt(np.diag(covariance))

print("a=", params[0],"+-", errors[0])
print("b=", params[1],"+-", errors[1])
print("c=", params[2],"+-", errors[2])
#print(" =", params[],"+-", errors[]

xplot=np.linspace(min(r-1),max(r+1))
plt.plot(xplot, f(xplot, *params), 'r-', label='Ausgleichskurve', linewidth=1)
plt.legend(loc="best")

plt.plot(r, U, "kx", label="Messwerte")
plt.xlabel(r"$ \mathrm{r} \, / \, \si{\centi\meter}")
plt.ylabel(r"$ \mathrm{U} \, / \, \si{\milli\volt}")
plt.legend(loc="best")
plt.xlim(min(r-1),max(r+1))
plt.ylim(0, max (U+0.5))
plt.xticks(np.arange(min(r), max(r+1), 2.0))
plt.yticks(np.arange(0, max(U), 0.5))
plt.grid()


plt.tight_layout()
plt.savefig("Bilder/Plot_Photodiode.pdf")
