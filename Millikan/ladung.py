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

r = np.array([ 4.1009,4.0796,4.0833,4.0771,4.0823,4.0758,4.0770,4.0847 ,4.0913])
q = np.array([ 4.1182,2.5909,1.5803,2.1580,2.0613,0.86241,0.85877,1.4684,1.6463])
# r = r*10**(-6) umrechnung in SI
q = q * 10**(-18)
e = 1.602*10**(-19)
plt.plot(r, q/e, 'x', color='red')
plt.xlabel(r'$r\,/\,\si{\micro\meter}$')
plt.ylabel(r'$q\,/\,e$')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('bilder/ladung.pdf')
