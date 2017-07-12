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

U1, I1 = np.genfromtxt('teilB.txt', skip_header = 1, unpack=True)
# If = 2.5
# Uf = 6
R = 1e6
Imax = 69e-9
I2 = I1*1e-9
I = np.log(I2/Imax)

U = U1 - R * I2
def f(m, U, n):
    return m * U + n
params, covariance =curve_fit(f,U,I)
errors = np.sqrt(np.diag(covariance))

print("m", params[0],"+-", errors[0])
print("n", params[1],"+-", errors[1])

plt.plot(U, f(U, *params), '-', color = 'blue', label='lineare Auslgeichsrechnung')
# U = np.log(U2 / Uf)
# def f(a, b, U):
#     return a * U + b
#
# params, covariance = curve_fit(f, U, I)
# errors = np.sqrt(np.diag(covariance))
#
# print("a=", params[0],"+-", errors[0])
# print("b=", params[1],"+-", errors[1])
# # U = np.log(U1)
# plt.plot(U, f(U, *params), '-', color='blue', label='linearer Ausgleichs')
plt.plot(U,I, 'x', color = 'red', label="Messwerte")
plt.xlabel(r"$U_\symup{G,korr}\,/\,\si{\volt}$")
plt.ylabel(r"$log(I/I_\symup{max})$")
plt.grid()
plt.legend()
plt.savefig("bilder/Kathodentemperatur.pdf")
