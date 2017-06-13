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
z_3 = z_3 * 1e-3
z_0 = 28.35e-3
z = z_3 - z_0
I_3 = I_3 * 1e-9 - 0.3e-9
L = 1
A_0 = 860e-9
lmbd = 532e-9
b = 0.15e-3



plt.plot(z/1e-3, I_3/1e-9, 'b-', label='gemessene Intensität')
plt.grid()
plt.xlabel(r'$\zeta - \zeta_0\,/\,\si{\milli\meter}$')
plt.ylabel(r'$I\,/\,\si{\nano\ampere}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/doppel2.pdf')
plt.show()
