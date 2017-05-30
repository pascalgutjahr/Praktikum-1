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

N0 = 1113 # für t = 1100s
N_0 = N0 / 1100 # für t = 1s
N_gamma = 131.62 # für t = 1s

N = np.array([6803, 10219, 7897, 7889, 6041, 3363, 3232, 2065, 1911, 1684])
d = np.array([0.1, 0.4, 1.03, 1.3, 2.01, 3.06, 3.45, 4.06, 4.56, 5.10])
t = np.array([60, 110, 180, 230, 400, 600, 700, 800, 900, 1000])

N = N / t - N_0 # auf t = 1s normiert und Nulleffekt abgezogen
N_log = np.log(N/N_gamma)

plt.plot(d, N_log, 'bx', label='Messwerte')

plt.grid()
plt.xlabel(r'$d \,/\, \si{\centi\meter}$')
plt.ylabel(r'$N \,/\,\si[per-mode=fraction]{\second}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/gammaPB.pdf')
plt.show()
