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
# g = np.array([ 17.6,  16.0,   18.4,  19.5,  21.2,  25.1,  17.3,  17.3,  18.7,  21.0 ])
# V1 = np.array([ 4.76,  4.6,   4.84,  4.95,  5.12,  5.51,  4.73,  4.73,  4.87,  5.1 ])
# b = np.array([ 87.4,  84.0,   76.6,  70.5,  63.8, 54.9, 92.7,  85.2,  73.8,  66.5])*10**(-2)
b = np.array([66.5, 73.8, 85.2, 92.7, 70.5, 76.6, 84.0, 87.4])*10**(-2) 
# V2 = np.array([ 11.74,  11.4,   10.66,  10.05,   9.38,   8.49,  12.27,  11.52,  10.38,   9.65])

# V1 = np.array([ 4.97,  5.25,  4.16,  3.62,  3.01,  2.19,  5.36,  4.92,  3.95,  3.17])
V2 = np.array([ 0.52,  0.57,  0.66,  0.78,  0.47,  0.56,  0.69,  0.82])
# V2 = np.array([0.82, 0.69, 0.56, 0.47, 1.16, 0.89, 0.78, 0.66, 0.57, 0.52])

def f(V2, m, n):
   return m * (1+V2) + n

params, covariance = curve_fit(f, V2, b)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

plt.plot(1+V2, f(V2, *params), 'k-', label='linearer Fit: b')

plt.plot(1+V2, b, '.', color='red')
plt.xlabel(r'$1 + V$')
plt.ylabel(r'$b´\,/\,\si{\meter}$')
plt.tight_layout()
plt.legend()
plt.grid()
plt.savefig('bilder/abbeB.pdf')
