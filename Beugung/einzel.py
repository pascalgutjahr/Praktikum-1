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

d = np.array([16.85,17.35,17.85,18.35,18.85,19.35,19.85,20.35,20.85,21.35,21.85,22.35,22.85,23.35,23.85,
24.35,24.85,25.35,25.85,26.35,26.85,27.35,27.60,27.85,28.10,28.35,28.60,28.85,29.10,29.35,29.85,30.35,30.85,31.35,31.85,
32.35,32.85,33.35,33.85,34.35,34.85,35.35,35.85,36.35,36.85,37.35,37.85,38.35,38.85,39.35,39.85])

I = np.array([3,2,1,2,4,7,8,7,4,2,6,14,24,28,21,8,6,42,120,280,490,
680,780,840,850,860,840,800,740,640,440,240,100,10,5,10,20,42,32,16,8,10,16,22,22,
16,8,4,5,8,12])

I = (I-0.3)*10**(-6)
d = d*1e-3
a = 860e-6
b = 0.15e-3
l = 1
lam = 532e-9
phi = (d - 0.02835) / l

j = a * ((np.sin((np.pi * b * np.sin(phi))/lam)) / ((np.pi * b * np.sin(phi)) / (lam)))**2


def f(d,a,b,l):
    return b*b*a*a*((l/(np.pi*a*np.sin((d-0.02835)/1))
    )*(l/(np.pi*a*np.sin((d-0.02835)/1))))*((np.sin(
    (np.pi*a*np.sin((d-0.02835)/1))/l))*(np.sin((np.pi*a*np.sin((d-0.02385)/1))/l)))

params, covariance= curve_fit(f, d, I)
errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('l =', params[2], '±', errors[2])

# plt.plot((d-0.02835),f(d,*params), '-', color = 'blueviolet', label='Ausgleichsgerade', linewidth=1)
plt.plot((d-0.02835), j*10**6, '-', color = "mediumturquoise", label = "Ausgleichskurve", linewidth = 1)
plt.plot((d-0.02835), I*10**6, 'x', color = "forestgreen", label = "Messwerte", linewidth = 1)

plt.xlabel(r'$\zeta - \zeta_0 \,/\,\si{\meter}$')
plt.ylabel(r'$I\,/\,\si{\micro\ampere}$')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("bilder/Einzelspalt.pdf")
