import numpy as np

t, T1, T2, pa, pb, N = np.genfromtxt('tabelle.txt', skip_header=2, unpack=True)

print('Mittelwert von N =', np.mean(N))
print('Standardabweichung von N =', np.std(N))
print('Varianz von N =', np.var(N))
