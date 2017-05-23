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

U = np.array([310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700])
N_60 = np.array([17919,18485,18816,19267,19079,18757,19033,19287,19307,19245,19330,19591,19648,19482,19597,19468,19688,19627,19439,19559,19427,19399,19492,19473,19583,19421,19640,19686,19718,19816,20138,19965,20213,20120,20105,20600,20600,20659,20611,21140])
N_1 = np.round((N_60 / 60),1)

U_fit = np.array([380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560])
N_fit = np.array([19287,19307,19245,19330,19591,19648,19482,19597,19468,19688,19627,19439,19559,19427,19399,19492,19473,19583,19421])/60


def f(U_fit, m, n):
   return m * U_fit + n

params, covariance = curve_fit(f, U_fit, N_fit)

errors = np.sqrt(np.diag(covariance))

print('m =', params[0], '+-', errors[0])
print('n =', params[1], '+-', errors[1])

plt.plot(U_fit, f(U_fit, *params), 'k-', label='linearer Fit')
# m = 0.0123 +- 0.0087
# n = 318.8 +- 4.1

DeltaN = np.sqrt(N_60) / 60
plt.plot(U, N_1, 'mx', label=r'Messwerte')
plt.errorbar(U,N_1, yerr=DeltaN, fmt='|')
plt.grid()
plt.xlabel(r'$U\,/\,\si{\volt}$')
plt.ylabel(r'$1\,/\,\si{\second}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('bilder/charakteristik.pdf')
plt.show()
