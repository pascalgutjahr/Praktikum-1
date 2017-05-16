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


plt.plot(t, streu45, 'bx', label='$45\,\%$ Pumpleistung')
plt.plot(t, streu70, 'rx', label='$70\,\%$ Pumpleistung')
plt.grid()
plt.xlabel(r'$t \,/\, \si{\micro\second}$')
plt.ylabel(r'Streuintensität $\,/\,1000 \cdot \si[per-mode=fraction]{\square\volt\per\second}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/streuintensitaet.pdf')
plt.show()
