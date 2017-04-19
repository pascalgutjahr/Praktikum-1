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

t, T1, T2, pa, pb, N = np.genfromtxt('tabelle.txt', unpack=True, skip_header = 3)

x_plot = np.linspace(min(t), max(t))


def f(t, a, b, c):
    return a*t**2 + b*t + c

params, covariance = curve_fit(f, t, T1)

errors = np.sqrt(np.diag(covariance))

print("a=", params[0], "+-", errors[0])
print("b=", params[1], "+-", errors[1])
print("c=", params[2], "+-", errors[2])

plt.plot(x_plot, f(x_plot, *params), 'r-', label='Regression T$_1$(t)', linewidth=1)


plt.plot(t, T1, 'rx', label='Temperatur des warmen Reservoirs')
plt.xlabel(r'$t\,/\,\si{\second}')
plt.ylabel(r'$T\,/\,\si{\kelvin}')
plt.xlim(min(t), max(t))
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('bilder/aurum.pdf')
