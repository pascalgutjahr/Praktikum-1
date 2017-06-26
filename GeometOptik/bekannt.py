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

g2 = np.array([85,75,70,65,60,50,45,35,30,25,15])
b2 = np.array([6.1,6.1,6.2,6.3,6.2,6.3,6.5,6.6,6.7,7.0,8.0])

x1 = np.array([0,0,0,0,0,0,0,0,0,0,0])
x2 = np.linspace(0,90,100)

a = -(6.1/85) * x2 + 6.1
b = -(75/6.1)**(-1) * x2 + 6.1
c = -(70/6.2)**(-1) * x2 + 6.2
d = -(65/6.3)**(-1) * x2 + 6.3
e = -(60/6.2)**(-1) * x2 + 6.2
f = -(50/6.3)**(-1) * x2 + 6.3
g = -(45/6.5)**(-1) * x2 + 6.5
h = -(35/6.6)**(-1) * x2 + 6.6
i = -(30/6.7)**(-1) * x2 + 6.7
j = -(25/7.0)**(-1) * x2 + 7.0
k = -(15/8.0)**(-1) * x2 + 8.0

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

plt.plot([4.2,4.2],[0,5.75], '--', color='olive', label="Brennweite")
plt.plot([0,4.2],[5.75,5.75], '--', color= 'olive', label="Brennweite")
plt.plot(5.5,5.5, ".", color='black', linewidth=5, label='berechneter Punkt')
plt.plot(5,5, ".", color='maroon', linewidth=5, label="Herstellerangabe" )
plt.xlabel(r'$g\,/\,\si{\centi\meter}$')
plt.ylabel(r'$b\,/\,\si{\centi\meter}$')
plt.tight_layout()
plt.legend()
plt.grid()
plt.ylim(0,9)
plt.xlim(0,20)
plt.savefig('bilder/bekannt.pdf')
