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
t = t*60
T1 = T1+273.5
T2 = T2+273.5

x_plot = np.linspace(min(t), max(t))


def f(t, a, b, c):
    return a*t**2 + b*t + c

params, covariance = curve_fit(f, t, T1)

errors = np.sqrt(np.diag(covariance))

print("a=", params[0], "+-", errors[0])
print("b=", params[1], "+-", errors[1])
print("c=", params[2], "+-", errors[2])

plt.plot(x_plot, f(x_plot, *params), 'r-', label='Regression T$_1$(t)', linewidth=1)


def g(t, d, e, f):
    return d*t**2 + e*t + f

params, covariance = curve_fit(g, t, T2)

errors = np.sqrt(np.diag(covariance))

print("d=", params[0], "+-", errors[0])
print("e=", params[1], "+-", errors[1])
print("f=", params[2], "+-", errors[2])

plt.plot(x_plot, g(x_plot, *params), 'b-', label='Regression T$_2$(t)', linewidth=1)

plt.plot(t, T1, 'rx', label='Temperatur des warmen Reservoirs')
plt.plot(t, T2, 'bx', label='Temperatur des kalten Reservoirs')
plt.xlabel(r'$t\,/\,\si{\second}')
plt.ylabel(r'$T\,/\,\si{\kelvin}')
plt.xlim(min(t), max(t))
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('Bilder/Plot1.pdf')
