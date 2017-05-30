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

t, v70, v45, streu70, streu45 = np.genfromtxt('werte.txt', unpack=True, skip_header=2)

d = [-0.42, 1.08, 1.83, 2.53, 3.33, 4.08, 4.83, 5.58, 6.33, 7.08]


plt.plot(d, streu45, 'bx', label='$45\,\%$ Pumpleistung')
plt.plot(d, streu70, 'rx', label='$70\,\%$ Pumpleistung')
plt.grid()
plt.xlabel(r'$d \,/\, \si{\milli\meter}$')
plt.ylabel(r'Streuintensität $\,/\,1000 \cdot \si[per-mode=fraction]{\square\volt\per\second}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/streuintensitaet.pdf')
plt.show()
