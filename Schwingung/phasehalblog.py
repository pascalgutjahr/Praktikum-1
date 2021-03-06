import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 13
plt.rcParams['lines.linewidth'] = 1
csfont = {'fontname': 'Times New Roman'}

# halblogarithmisch
fre, t = np.genfromtxt('tables/phase.txt', unpack=True, skip_header=2)

fre *= 1000
t /= 1e6
phirad = 2 * np.pi * fre * t

# Theoriekurve
# L = 3.53 * (10**-3)
# C = 5.015 * (10**-9)
# w = fre * 2 * np.pi
# R = 271.6
# # fre = np.linspace(np.log(15),np.log(20))
# phi = np.arctan((w * R * C)/(1 - (L * C * (w**2))))
# # bis zur Resonanz plotten
#
# #plt.plot(fre/1000, phi, 'b-', label='Theoriekurve')
# # plt.plot(fre/1000, -phi, 'b-', label='Theoriekurve')
# fre_theo = np.linspace(15000, 37500, 100)
# phi_theo = np.arctan((2*np.pi*fre_theo * R * C)/(1 - (L * C * ((2*np.pi*fre_theo)**2))))
# fre_theo2 = np.linspace(38000, 55000, 100)
# phi_theo2 = np.arctan((2*np.pi*fre_theo2 * R * C)/(1 - (L * C * ((2*np.pi*fre_theo2)**2))))+np.pi
#
#
plt.plot(fre/1000, phirad, 'rx', label='Messwerte')
# plt.plot(fre_theo/1000, phi_theo, 'b-', label='Theoriekurve')
# plt.plot(fre_theo2/1000, phi_theo2, 'b-', label='Theoriekurve')

plt.yticks(np.arange(0, 5 * np.pi/4, np.pi/4), ['$0$', '$\mathrm{\pi}/4$', '$\mathrm{\pi}/2$', '$3\mathrm{\pi}/4$','$\mathrm{\pi}$'])
plt.xscale('log')
plt.xlabel(r'$\mathrm{\nu} \,/\, \mathrm{kHz}$')
plt.ylabel(r'$\mathrm{\varphi}$')
plt.xlim()
plt.legend(loc='lower right')
plt.grid()
plt.tight_layout()
plt.savefig('Bilder/phasehalblog.pdf')
plt.show()
