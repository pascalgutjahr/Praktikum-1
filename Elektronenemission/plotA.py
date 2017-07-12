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

U, I1, I2, I3, I4, I5 = np.genfromtxt('teilA.txt', skip_header = 1, unpack=True)

plt.plot(U, I1, 'x', color = 'red', label = r'$I_\symup{f,1}=1,8\si{\ampere}$')
plt.plot(U, I2, 'x', color = 'blue', label = r'$I_\symup{f,2}=1,9\si{\ampere}$')
plt.plot(U, I3, 'x', color = 'green', label = r'$I_\symup{f,3}=2,0\si{\ampere}$')
# plt.plot(U, I4, 'x', color = 'purple', label= r'$I_\symup{f,4}=2,2\si{\ampere}$')
# plt.plot(U, I5, 'x', color = 'black', label= r'$I_\symup{f,5}=2,4\si{\ampere}$')
plt.xlabel(r'$U\,/\,\si{\volt}$')
plt.ylabel(r'$I\,/\,\si{\micro\ampere}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('bilder/kennlinie.pdf')
