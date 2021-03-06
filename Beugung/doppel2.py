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

a,b,c,d, x, I = np.genfromtxt("werte.txt", unpack = True, skip_header = 4)

I = (I-0.3)*10**(-9)
x = x*10**(-3)
a = 90*10**(-9)
b = 0.15*10**(-3)
s = 0.25*10**(-3)
l = 1
lam = 532 * 10**(-9)
phi = (x - 0.02885) / l
d=np.linspace(-0.006,0.0065,1000)
#d1 = np.linspace(22.65, 35.15, 1000)
phii = d/l
#j = a * ((np.sin((np.pi * b * np.sin(phi))/lam)) / ((np.pi * b * np.sin(phi)) / (lam)))**2
T = 4*(np.cos((np.pi*s*np.sin(phii))/lam)**2) * (lam/(np.pi*b*np.sin(phii)))**2 * (np.sin((np.pi*b*np.sin(phii))/lam))**2

#def f(x,a,b,l):
#    return 4*(np.cos((np.pi*a*np.sin((x - 0.041) / 0.885))/l))**2 * (l/(np.pi*b*np.sin((x - 0.041) / 0.885)))**2 * (np.sin((np.pi*b*np.sin((x - 0.041) / 0.885))/l))**2
#    #a=s,b=b,l=lam
#params, covariance= curve_fit(f, x, I)
#errors = np.sqrt(np.diag(covariance))

#print('a =', params[0], '±', errors[0])
#print('b =', params[1], '±', errors[1])
#print('l =', params[2], '±', errors[2])
#print("T=",T)
#plt.plot((x-0.041),f(x, *params), '-', color = 'blueviolet', label='Ausgleichsgerade', linewidth=1)
plt.plot(d, T*20, '-', color = "mediumturquoise", label = "Theoriekurve", linewidth = 1)
plt.plot((x-0.02885), I*10**9, 'x', color = "forestgreen", label = "Messwerte", linewidth = 1)

plt.xlabel(r'$\zeta - \zeta_0 \,/\,\si{\meter}$')
plt.ylabel(r'$I\,/\,\si{\nano\ampere}$')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("bilder/Doppelspalt2.pdf")
