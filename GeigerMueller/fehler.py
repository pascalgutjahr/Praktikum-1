import numpy as np

N_60 = np.array([17919,18485,18816,19267,19079,18757,19033,19287,19307,19245,19330,19591,19648,19482,19597,19468,19688,19627,19439,19559,19427,19399,19492,19473,19583,19421,19640,19686,19718,19816,20138,19965,20213,20120,20105,20600,20600,20659,20611,21140])
N_1 = N_60 / 60
N_list = np.vstack(N_1)
print('Impulsrate pro Sekunde:',N_list)

# U = np.array([])
