import numpy as np
# import uncertainties.unumpy as unp
# from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

plt.subplot(2, 1, 1)

phi, U_max, U_out = np.genfromtxt('data1.txt', unpack=True, skip_header=3)
# in Bogenmaß umrechnen:
phiB = phi * 2 * np.pi / 360
# U *= 1e-3
# U_out = 2 / np.pi * U * np.cos(phi)
# print(U_out)


# def f(U, A, phi):
#    return A * np.cos(phi)

# params, covariance = curve_fit(f, np.cos(phi), U)

# errors = np.sqrt(np.diag(covariance))

# print('A =', params[0], '+-', errors[0])
# print('n =', params[1], '+-', errors[1])

# x_plot = np.linspace(min(np.cos(phi)), max(np.cos(phi)))

plt.plot(phiB, U_out, 'k.', label='Ohne Rauschen')
# plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')


plt.ylabel(r'$U_{out} \; \cdot 10^{-3}\,/\, V$')
plt.xlabel(r'$\cos{{(\phi)}}$')
plt.legend()

plt.grid()
plt.subplot(2, 1, 2)

phi2, U2_max, U2_out = np.genfromtxt('Rausch.txt', unpack=True, skip_header=2)
phi2B = phi2 * 2 * np.pi / 360
# U2 *= 1e-4
# U2_out = 2 / np.pi * U2 * np.cos(phi2)
# print(U2_out)


plt.plot(np.cos(phi2B), U2_out, 'k.', label='mit Rauschen')
plt.ylabel(r'$U_{out} \, \cdot 10^{-4} \,/\, V$')
plt.xlabel(r'$\cos{{(\phi)}}$')
plt.legend()
plt.grid()
plt.savefig('Bilder/phi.pdf')
plt.show()
