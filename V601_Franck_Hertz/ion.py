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

U=np.array([0,2.7,5.4,8.1,10.8,13.5,16.2,18.9,21.6,24.3,27,29.7,32.4,35.1,37.8,39.2])
U=U+18
I=np.array([0,0.02,0.05,0.12,0.19,0.31,0.44,0.61,0.81,1.06,1.31,1.61,1.97,2.32,2.78,3])
I*=1e-9
AU=np.array([27,29.7,32.4,35.1,37.8,39.2])
AU=AU+18
AI=np.array([1.31,1.61,1.97,2.32,2.78,3])
AI*=1e-9
#def f(AU, m, n):
 #   return m * AU + n

#params, covariance = curve_fit(f, AU, AI)

#errors = np.sqrt(np.diag(covariance))

#print('m =', params[0], '+-', errors[0])
#print('n =', params[1], '+-', errors[1])

#x_plot = np.linspace(min(AU), max(AU))

#plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
#m = 1.39392760981e-10 +- 5.04887352252e-12
#n = -5.01837361587e-09 +- 2.61093484622e-10
x=np.linspace(min(U), max(U))
y = 1.3939e-10*x-5.01837e-9
plt.plot(x,y, 'b-', label='Ausgleichsgerade')
plt.plot(U,I, 'r.', label='Messwerte')
plt.xlabel(r'$U_\symup{B}\,/\,\si{\volt}$')
plt.ylabel(r'$I_\symup{A}\,/\,\si{\nano\ampere}$')
plt.ylim(0,3e-9)
# plt.title('Messungen')
plt.grid()
# plt.legend('loc.best')
plt.tight_layout()
plt.savefig('bilder/ion.pdf')
plt.show()
