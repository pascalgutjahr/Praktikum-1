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
z_1 = z_1 * 1e-3
z_0 = 28.35e-3
z = z_1 - z_0
I_1 = I_1 * 1e-9 - 0.3e-9
L = 1
A_0 = 860e-9
lmbd = 532e-9
b = 0.15e-3

def f(z_1,A_0,b,lmbd):
    return b*b*A_0*A_0*((lmbd/(np.pi*A_0*np.sin((z_1-28.35e-3)/1)))*(lmbd/(np.pi*A_0*np.sin((z_1-28.35e-3)/1))))*((np.sin((np.pi*A_0*np.sin((z_1-28.35e-3)/1))/lmbd))*(np.sin((np.pi*A_0*np.sin((z_1-28.35e-3)/1))/lmbd)))
params, covariance= curve_fit(f, z, I_1)
errors = np.sqrt(np.diag(covariance))

print('A_0 =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('lmbd =', params[2], '±', errors[2])
plt.plot(z, f(z,*params), 'k-', label='Ausgleichskurve')

# B = A_0**2 * b**2 * (lmbd / (np.pi * b * np.sin(z)))**2 * np.sin(np.pi * b * np.sin(z)/lmbd)**2

j = A_0 * ((np.sin((np.pi * b * np.sin(z))/lmbd)) / ((np.pi * b *
np.sin(z)) / (lmbd)))**2

plt.plot(z, j, 'r-', label='Theoriekurve')

plt.plot(z, I_1, 'bx', label='gemessene Intensität')
plt.grid()
plt.xlabel(r'$\zeta - \zeta_0\,/\,\si{\milli\meter}$')
plt.ylabel(r'$I\,/\,\si{\nano\ampere}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/einzel.pdf')
plt.show()
