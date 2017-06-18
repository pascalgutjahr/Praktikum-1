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
z_2 = z_2 * 1e-3
z_0 = 28.90e-3
z = z_2 - z_0
I_2 = I_2 * 1e-9 - 0.3e-9
l = 1
A_0 = 970e-9
lmbd = 532e-9
b = 0.1e-3
s = 0.4e-3

def f(z_2,a,b,l):
    return 4*(np.cos((np.pi*a*np.sin((z_2 - 0.041) / 0.885))/l))**2 * (l/(np.pi*b*np.sin
    ((z_2 - 0.041) / 0.885)))**2 * (np.sin((np.pi*b*np.sin((z_2 - 0.041) / 0.885))/l))**2

params, covariance= curve_fit(f, z_2, I_2)
errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('l =', params[2], '±', errors[2])
# print("T=",T)



B = np.sqrt(4 * np.cos(np.pi*s*np.sin(z)/lmbd)**2 * (lmbd/np.pi*b*np.sin(z))**2 * np.sin(np.pi*b*np.sin(z)/lmbd)**2)
b = 4 * A_0 * np.cos(z/2)**2
plt.plot(z/1e-3, B/1e-9, 'r-', label='Theoriekurve')
plt.plot((z_2-0.041),f(z_2, *params), '-', color = 'blueviolet', label='Ausgleichsgerade', linewidth=1)
plt.plot(z/1e-3, I_2/1e-9, 'bx', label='gemessene Intensität')
plt.grid()
plt.xlabel(r'$\zeta - \zeta_0\,/\,\si{\milli\meter}$')
plt.ylabel(r'$I\,/\,\si{\nano\ampere}$')
plt.legend(loc='best')

plt.tight_layout
plt.savefig('bilder/doppel1.pdf')
plt.show()
