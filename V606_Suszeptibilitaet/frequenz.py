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

f, UA = np.genfromtxt('Mess1.txt', unpack=True, skip_header = 3)

UE = 0.41
UA = UA / 1000
U = UA / UE

# \nu_- bei 34.85
# \nu_+ bei 35.35
# \nu_0 bei 35.10

plt.plot(f, U, 'rx', label='Messwerte')
# plt.plot((32, 38), (1, 1), 'b--')
plt.plot((34,36), (1/np.sqrt(2), 1/np.sqrt(2)), 'b--')
plt.plot((34.85, 34.85), (0, 1/np.sqrt(2)), 'b--')
plt.plot((35.35, 35.35), (0, 1/np.sqrt(2)), 'b--')


plt.yticks([0, 0.25, 0.5, 1/np.sqrt(2), 1.0, 1.25], ['$0$', r'$0.25$',
r'$0.50$', r'$\frac{1}{\sqrt{2}}$', r'$1.00$', r'$1.25$'])
plt.xticks([32, 33, 34, 34.85, 35.35, 36], ['$32$', r'$33$',r'$34$', r'$34.85$',
r'$35.35$', r'$36$'])
plt.ylabel(r'$\frac{U_\symup{A}}{U_\symup{E}}')
plt.xlabel(r'$\nu \,/\,\si{\kilo\hertz}')
plt.xlim(32.8, 36.2)
# plt.ylim(850, 1650)
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('bilder/frequenz.pdf')
plt.clf()

plt.plot(f, UA*1000, 'bx', label='Messwerte')
plt.plot((32, 36), (475/np.sqrt(2), 475/np.sqrt(2)), 'g--')
plt.xlabel(r'$Frequenz\,/\,\si{\kilo\hertz}$')
plt.ylabel(r'$U_\symup{A}\,/\,\si{\milli\volt}$')
plt.xlim(32.8, 36.2)
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('bilder/frequenz_ohne_U_E.pdf')
