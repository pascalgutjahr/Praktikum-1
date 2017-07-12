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

U = np.array([5,10,15,20,25,30,35,40,45,50,60]) #
I2 = np.array([8,50,112,192,287,396,503,603,692,782,942]) #
If = 2.5
Is = 942e-6
Uf = 6
R = 1e6
# Imax = 69e-9
I1 = I2*1e-6
I = np.log(I1/Is)
U = np.log(U)

def f(m, U, n):
    return m * U + n
params, covariance =curve_fit(f,U,I)
errors = np.sqrt(np.diag(covariance))

print("m", params[0],"+-", errors[0])
print("n", params[1],"+-", errors[1])

plt.plot(U, f(U, *params), '-', color = 'blue', label="linearer Ausgleich")

plt.plot(U,I,'x', color = 'red', label = "Messwerte")
plt.xlabel(r"$log(U_\symup{A})$")
plt.ylabel(r"$log(I/I_\symup{s})$")

plt.grid()
plt.legend()
plt.savefig('bilder/langmuir.pdf')
