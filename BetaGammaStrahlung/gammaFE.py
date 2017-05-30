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

N = np.array([6108, 6781, 7099, 8057, 8470, 8471, 7762, 7170, 6170, 5339])
d = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
t = np.array([60, 90, 120, 180, 240, 300, 360, 400, 450, 500])

N = (N-N_0) / t  # auf t = 1s normiert und Nulleffekt abgezogen
N_log = np.log(N/N_gamma)

F = np.sqrt(N) / t
print('Fehler Eisen:', np.vstack(F))

def f(d, a, b):
    return a * d + b

params, covariance = curve_fit(f, d, N_log)

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
plt.plot(d, f(d,*params), '-',color='deeppink', label='Lineare Ausgleichsrechnung')

plt.plot(d, N_log, 'bx', label='Messwerte für Eisenabsorber')

plt.grid()
plt.xlabel(r'$d \,/\, \si{\centi\meter}$')
plt.ylabel(r'$\log{(\frac{N-N_0}{N_\symup{ohne}})}$') # N_ohne: Zählrate ohne Absorber, N_0: Zählrate ohne Strahler
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/gammaFE.pdf')
plt.show()
