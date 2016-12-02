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

U, I = np.genfromtxt('data1.txt', unpack=True, skip_header=2)

U /=1000   # in Volt
I /=1000   # in Ampere

def f(U, m, n):
    return m * U + n

params, covariance = curve_fit(f, U, x)

errors = np.sqrt(np.diag(covariance))
