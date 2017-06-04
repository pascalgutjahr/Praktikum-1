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

t, d, dd, N = np.genfromtxt("werte.txt", unpack=True, skip_header = 3)

d2 = np.linspace(100, 295)
d3 = np.linspace(275, 450)
d4 = np.array([102, 126, 153, 160, 200, 253])
d5 = np.array([302, 338, 400, 444])

N2 = np.array([-9.43, -8.78, -9.86, -10.66])
N3 = np.array([-2.57, -3.23, -4.07, -4.71, -5.90, -7.60])
Nt = N/t
Nt2 = np.log((Nt - 0.52) / (554.29))

DeltaN = np.sqrt(Nt2)

#d = d*10**(-6)
#d4 = d4*10**(-6)
#d5 = d5*10**(-6)
#
#
#
#def g(d5, a, b):
#    return a * d5 + b
#
#params, covariance = curve_fit(g, d5, N2)
#errors = np.sqrt(np.diag(covariance))
#
#print ("a=", params[0] ,"+-", errors[0])
#print ("b=", params[1] ,"+-", errors[1])
#plt.plot(d5, g(d5, *params), 'b--', label='Ausgleichsgerade', linewidth=1)
#
#
#def f(d4, m, c):
#    return m * d4 + c
#
#params, covariance = curve_fit(f, d4, N3)
#errors = np.sqrt(np.diag(covariance))
#
#print ("m=", params[0] ,"+-", errors[0])
#print ("c=", params[1] ,"+-", errors[1])
#plt.plot(d4, f(d4, *params), 'b--', label='Ausgleichsgerade', linewidth=1)


h = -0.0102920133134 * d3 -5.86416306158
i = -0.0339349530518 * d2 + 0.941890555201

plt.plot(d3, h, "--", linewidth = 1, color = "goldenrod", label =
"lineare Augleichsrechnung")
plt.plot(d2, i, "--", color = "goldenrod", linewidth = 1)

plt.plot(d, Nt2, "x", linewidth=.5, color = "darkslategrey", label=
"Absorptionskurve")
plt.plot((287.868, 287.868), (-11, -8.895788922), "--", linewidth = 1,
color = "black")
plt.errorbar(d,Nt2, yerr = DeltaN, fmt='|', color = "darkslategrey")

plt.xlabel(r'$d\,/\,\si{\micro\meter}$')
plt.ylabel(r'$\log{\left(\frac{N - N_\text{0}}{N_\text{ohne}}\right)}$')
plt.xticks([100, 150, 200, 250, 287.87, 350, 400, 450],
          [r'$100$', r'$150$', r'$200$', r'$250$', r'$R_\text{max}$',
r'$350$', r'$400$', r'$450$'])
plt.grid()
plt.legend()
plt.ylim(-11, -2)
plt.tight_layout()
plt.savefig("bilder/betaAl.pdf")
print(Nt)
