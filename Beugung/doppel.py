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

x = np.array([22.65,22.90,23.15,23.40,23.65,23.90,24.15,24.40,24.65,24.90,25.15,25.40,
25.65,25.90,26.15,26.40,26.65,26.90,27.15,27.40,27.65,27.90,28.15,28.40,28.65,28.90,29.15,
29.40,29.65,29.90,30.15,30.40,30.65,30.90,31.15,31.40,31.65,31.90,32.15,32.40,32.65,32.90,
33.15,33.40,33.65,33.90,34.15,34.40,34.65,34.90,35.15])


I = np.array([32.0, 14.0,  4.4,  5.0,  3.6,  1.8,  2.0,  8.0, 30.0, 40.0,
2.0,  4.0,160.0,210.0,100.0,100.0,380.0,540.0,270.0,140.0,550.0,860.0,530.0,200.0,780.0,970.0,740.0,240.0,420.0,
840.0,720.0,250.0,250.0,540.0,520.0,210.0,120.0,220.0,240.0,120.0, 50.0,
64.0, 65.0, 41.0, 22.0, 10.0,
  6.0, 10.0,  9.0,  9.0, 10.0])

I = (I-0.3)*10**(-9)
x = x*10**(-3)
a = 970*10**(-9)
b = 0.1*10**(-3)
s = 0.4*10**(-3)
l = 1
lam = 532 * 10**(-9)
phi = (x - 0.0289) / l
d=np.linspace(-0.007,0.007,1000)
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
plt.plot(d, T*250, '-', color = "mediumturquoise", label = "Theoriekurve", linewidth = 1)
plt.plot((x-0.0289), I*10**9, 'x', color = "forestgreen", label = "Messwerte", linewidth = 1)

plt.xlabel(r'$\zeta - \zeta_0 \,/\,\si{\meter}$')
plt.ylabel(r'$I\,/\,\si{\nano\ampere}$')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("bilder/Doppelspalt1.pdf")
