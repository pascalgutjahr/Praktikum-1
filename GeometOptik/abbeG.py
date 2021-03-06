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

# V1 = 1 + 1/V
# V2 = 1 + V
g = np.array([ 17.6,  16.0,   18.4,  19.5,  21.2,  25.1,  17.3,  17.3,  18.7,  21.0 ])*10**(-2)
# V1 = np.array([ 4.76,  4.6,   4.84,  4.95,  5.12,  5.51,  4.73,  4.73,  4.87,  5.1 ])
# b = np.array([ 87.4,  84.0,   76.6,  70.5,  63.8,  54.9,  92.7,  85.2,  73.8,  66.5])
# V2 = np.array([ 11.74,  11.4,   10.66,  10.05,   9.38,   8.49,  12.27,  11.52,  10.38,   9.65])

V1 = np.array([ 4.97,  5.25,  4.16,  3.62,  3.01,  2.19,  5.36,  4.92,  3.95,  3.17])


def f(V1, m, n):
   return m * (1+ 1/V1) + n

params, covariance = curve_fit(f, V1, g)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

plt.plot(1+1/V1, f(V1, *params), 'k-', label='linearer Fit: g')


plt.plot(1+1/V1, g, '.', color='green')
plt.xlabel(r'$1 + \frac{1}{V}$')
plt.ylabel(r'$g´\,/\,\si{\meter}$')
plt.tight_layout()
plt.legend()
plt.grid()
plt.savefig('bilder/abbeG.pdf')
