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

nu15, v15, nu30, v30, nu60, v60 = np.genfromtxt('wertedick.txt', unpack=True, skip_header=2)
# dickes Rohr
nu15 = nu15 / np.cos(1.397)
nu30 = nu30 / np.cos(1.231)
nu60 = nu60 / np.cos(0.955)

plt.plot(v15, nu15/1000, 'bx', label=r'$\theta = 15\,\si{\degree}$ Winkel')
plt.plot(v30, nu30/1000, 'rx', label=r'$\theta = 30\,\si{\degree}$ Winkel')
plt.plot(v60, nu60/1000, 'gx', label=r'$\theta = 60\,\si{\degree}$ Winkel')
plt.grid()
plt.xlabel(r'$v \,/\,\si[per-mode=fraction]{\meter\per\second}$')
plt.ylabel(r'$\frac{\Delta\nu}{\cos{\alpha}}\,/\,\si{\kilo\hertz}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/winkeldick.pdf')
plt.show()
