import matplotlib as mpl
from scipy.optimize import curve_fit
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.rcParams['lines.linewidth'] = 1
import numpy as np
mpl.rcParams.update({
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}'
})

Z, T = np.genfromtxt('txt/plot.txt', unpack=True, skip_header = 3)
# T = Winkel Theta, Z = Ordnungszahl

The = 2 *np.pi * T / 360 # Winkel in rad
h = 6.626 *10**(-34)
c = 299729458
d = 201 *10**(-12)
e = 1.602 *10**(-19)
E_K = (h*c) / (2*d*np.sin(The)) / e

W = np.sqrt(E_K)
Z2 = Z**2

x_plot = np. linspace(90, 130)

def f(W, m, b):
    return m*W + b

params, covariance = curve_fit(f, W, Z2)

errors = np.sqrt(np.diag(covariance))

print("m=", params[0], "+-", errors[0])
print("b=", params[1], "+-", errors[1])

# m= 22.9616004655 +- 3.5769453201
# b= -1348.56433773 +- 404.895551595

plt.plot(x_plot, f(x_plot, *params), 'r-', label='lineare Regression', linewidth=1)


plt.plot(W, Z2, 'rx', label='Messwerte')
plt.plot()
plt.ylabel(r'$Z^2')
plt.xlabel(r'$\sqrt{E_K}\,/\,\sqrt{\si{\electronvolt}}')
plt.xlim(min(W)-2, max(W)+2)
plt.ylim(850, 1650)
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('bilder/plot.pdf')
