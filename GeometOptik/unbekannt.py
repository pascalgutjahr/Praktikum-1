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

g2 = np.array([85,75,70,65,60,50,45,35,30,15,10])
b2 = np.array([8,7.9,7.8,7.9,7.9,8.1,8.3,8.4,8.9,10.8,14.2])

x1 = np.array([0,0,0,0,0,0,0,0,0,0,0])
x2 = np.linspace(0,90,100)

a = -(85/8.0)**(-1) * x2 + 8.0
b = -(75/7.9)**(-1) * x2 + 7.9
c = -(70/7.8)**(-1) * x2 + 7.8
d = -(65/7.9)**(-1) * x2 + 7.9
e = -(60/7.9)**(-1) * x2 + 7.9
f = -(50/8.1)**(-1) * x2 + 8.1
g = -(45/8.3)**(-1) * x2 + 8.3
h = -(35/8.4)**(-1) * x2 + 8.4
i = -(30/8.9)**(-1) * x2 + 8.9
j = -(25/10.8)**(-1) * x2 + 10.8
k = -(15/14.2)**(-1) * x2 + 14.2

plt.plot(g2,x1, 'x', color='limegreen')
plt.plot(x1,b2, 'x', color='limegreen')

plt.plot(x2, a, '-', color='darksalmon')
plt.plot(x2, b, '-', color='darksalmon')
plt.plot(x2, c, '-', color='darksalmon')
plt.plot(x2, d, '-', color='darksalmon')
plt.plot(x2, e, '-', color='darksalmon')
plt.plot(x2, f, '-', color='darksalmon')
plt.plot(x2, g, '-', color='darksalmon')
plt.plot(x2, h, '-', color='darksalmon')
plt.plot(x2, i, '-', color='darksalmon')
plt.plot(x2, j, '-', color='darksalmon')
plt.plot(x2, k, '-', color='darksalmon')

plt.plot([7.5,7.5],[0,7], '--', color='olive', label="Brennweite)
plt.plot([0,7.5],[7,7], '--', color= 'olive', label="Brennweite)
plt.plot(6.8,6.8, ".", color='black', linewidth=5, label='berechneter Punkt')
plt.tight_layout()
plt.legend()
plt.grid()
plt.ylim(0,20)
plt.xlim(0,86)
plt.savefig('bilder/unbekannt.pdf')
