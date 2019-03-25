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

U = [350, 400, 450, 500, 550, 600, 650, 700]
Q = [0.39, 0.78, 1.14, 1.53, 2.10, 2.46, 2.79, 3.19]

plt.plot(U, Q, 'mx', label=r'Messwerte')
# plt.errorbar(U,N_1, yerr=DeltaN, fmt='|')
plt.grid()
plt.xlabel(r'$U\,/\,\si{\volt}$')
plt.ylabel(r'$Q\,/\,\symup{e}\,\cdot 10^{16}\,\si{\coulomb}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('bilder/ladung.pdf')
plt.show()
