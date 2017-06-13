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

z_1, I_1, z_2, I_2, z_3, I_3 = np.genfromtxt('werte.txt', unpack=True, skip_header=2)
z_1 = z_1e-2
z_0 = 28.35e-2
z = z_1 - z_0

# def f(d, a, b):
#     return a * d + b
#
# params, covariance = curve_fit(f, d, N_log)
#
# errors = np.sqrt(np.diag(covariance))
#
# print('a =', params[0], '±', errors[0])
# print('b =', params[1], '±', errors[1])
# plt.plot(d, f(d,*params), '-',color='deeppink', label='Lineare Ausgleichsrechnung')

plt.plot(z, I_1, 'bx', label='gemessene Intensität')

plt.grid()
plt.xlabel(r'$\zeta\,/\,\si{\milli\meter}$')
plt.ylabel(r'$I\,/\,\si[per-mode=fraction]{\nano\ampere}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/einzel.pdf')
plt.show()
