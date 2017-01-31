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

T = np.array([14.15,11.08,9.648,8.619,7.86,7.21,6.86,6.50,6.11,5.6])

I = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

mu = 1.256637061 * 10**(-6)
R = 0.078
N = 390
B = mu *  (N * 8 * I)/(np.sqrt(125) * R)
# T = T * 10**6
B = B * 10**3

T = 1/T**2

# m= 0.159 ± 0.005
# b= -0.00033 ± 0.00001

def f(m, T, b):
    return m*T+b

params, covariance = curve_fit(f, T, B)
errors = np.sqrt(np.diag(covariance))

print('m=', params[0], '±', errors[0])
print('b=', params[1], '±', errors[1])

plt.plot(T, f(T,*params),'k-', label='Ausgleichsgerade', linewidth=1)
plt.plot(T, B, 'rx', label= 'Messwerte')
plt.xlabel(r'$\frac{1}{T^2} \,/\,\si{\per\square\second}')
plt.ylabel(r'$B \,/\,\si{\milli\tesla}')
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.show()
plt.savefig('bilder/Bplot.pdf')
