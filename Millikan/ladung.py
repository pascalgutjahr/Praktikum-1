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

r = np.array([0.74867,0.59342,0.6092,0.524,0.5931,0.51057,0.5290,0.6180,0.6787])
q = np.array([22.597,5.989,5.9240,7.6378,8.0430,2.6169,2.7198,6.0503,7.7653])
# r = r*10**(-7) umrechnung in SI
q = q * 10**(-19)
e = 1.602*10**(-19)
plt.plot(r, q/e, 'x', color='red')
plt.xlabel(r'$r\,/\,\si{\micro\meter}$')
plt.ylabel(r'$q\,/\,e$')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('bilder/ladung.pdf')
